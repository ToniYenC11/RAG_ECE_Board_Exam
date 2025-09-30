"""
This is a script to extract the datasets in various formats from the Datasets folder. To extract efficiently, I have considered the following document extractors:

1. **[Markitdown](https://github.com/microsoft/markitdown)**- MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines. To this end, it is most comparable to textract, but with a focus on preserving important document structure and content as Markdown (including: headings, lists, tables, links, etc.)
    - Supports PDF, pptx, docx, xls, images (EXIF metadata and OCR), audio, HTML, Text-based (CSV,JSON,XML), zip, YT urls, EPubs, and more
2. **[Docling](https://github.com/docling-project/docling)** - Docling simplifies document processing, parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the gen AI ecosystem.
    - Parsing of multiple document formats incl. PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, VTT, images (PNG, TIFF, JPEG, ...), and more
"""


import os
import sys
import argparse
import logging
import datetime
from docling.document_converter import DocumentConverter
#from markitdown import MarkItDown
import torch

torch.device("cpu")

def setup_logging(output_file):
    """Set up logging to both terminal and file."""
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Log all messages (INFO, DEBUG, ERROR, etc.)

    # Create a console handler and set level to debug
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Create a file handler and set level to debug
    file_handler = logging.FileHandler(output_file)
    file_handler.setLevel(logging.DEBUG)  # Log all messages to file

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def is_file_in_log(target_path, log_file_path):
    """Check if a file path is already recorded in the log file.
    
    Args:
        target_path (str): Path of the file to check
        log_file_path (str): Path to the log file
    
    Returns:
        bool: True if file is found in log, False otherwise
    """
    if not os.path.exists(log_file_path):
        return False
    
    try:
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            processed_files = {line.strip() for line in log_file if line.strip()}
            return str(target_path) in processed_files
    except Exception as e:
        logging.warning(f"Error reading log file {log_file_path}: {e}")
        return False

def add_to_log(target_path, log_file_path):
    """Add a successfully converted file path to the log file.
    
    Args:
        target_path (str): Path of the successfully converted file
        log_file_path (str): Path to the log file
    """
    try:
        # Ensure the log file directory exists
        log_dir = os.path.dirname(log_file_path)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{target_path}\n")
            
    except Exception as e:
        logging.error(f"Error writing to log file {log_file_path}: {e}")

def convert_md(target_path, md_converter, check_path, log_file_name="conversion_log.txt", *args):
    """Convert the file into markdown with existence checking and logging.

    Args:
        target_path (Path): Absolute path of the file to convert
        md_converter (_type_): Defined in the md, which may be either Docling or Markitdown.
        check_path (Path): Path to the directory structure where converted files should be checked
        log_file_name (str): Name of the log file (will be placed in ../logs/ directory)
    """
    
    # Create log file path in logs directory one level up from src
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(os.path.dirname(current_dir), 'logs')
    log_file_path = os.path.join(logs_dir, log_file_name)
    
    # Get the base directory and file name of the target path
    base_dir = os.path.dirname(target_path)
    base_name = os.path.basename(target_path)
    
    # Replace file extension to '.md'
    md_file_name = os.path.splitext(base_name)[0] + '.md'
    
    # Find the 'Datasets' folder in the path
    # Assuming structure is: .../Datasets/GEAS/Chemistry/file.pdf
    path_parts = os.path.normpath(target_path).split(os.sep)
    
    try:
        datasets_index = path_parts.index('Datasets')
    except ValueError:
        logging.error(f"'Datasets' folder not found in path: {target_path}")
        return
    
    # Get the path from Datasets onwards (e.g., GEAS/Chemistry)
    relative_path = os.path.join(*path_parts[datasets_index + 1:-1])
    
    # Define the new root directory for markdown files (Datasets_md)
    # It should be at the same level as Datasets folder
    root_path = os.sep.join(path_parts[:datasets_index])
    root_md_dir = os.path.join(root_path, 'Datasets_md')
    
    # Create the full path maintaining subfolder structure
    md_folder = os.path.join(root_md_dir, relative_path)
    
    # Full path for the markdown file in the 'Datasets_md' structure
    md_txt = os.path.join(md_folder, md_file_name)
    
    # Check if file already exists in log file (primary check)
    if is_file_in_log(target_path, log_file_path):
        logging.info(f"File {target_path} already processed according to log file. Skipping conversion.")
        return
    
    # Secondary check: verify if the markdown file actually exists in the check_path
    expected_md_path = os.path.join(check_path, relative_path, md_file_name)
    if os.path.exists(expected_md_path):
        logging.info(f"Markdown file {expected_md_path} already exists. Skipping conversion.")
        # Add to log file if it exists but wasn't logged
        add_to_log(target_path, log_file_path)
        return
    
    # Ensure the target subfolder exists inside 'Datasets_md'
    os.makedirs(md_folder, exist_ok=True)
    
    # Call converter
    converter = md_converter()
    
    # Convert and save the markdown content
    try:
        result = converter.convert(target_path)
        logging.info(f"Successfully converted {target_path}")
    except Exception as e:
        logging.error(f"Error converting file {target_path}: {e}")
        return

    # Write the result to the markdown file
    try:
        with open(md_txt, 'w', encoding='utf-8') as md_file:
            md_file.write(result.document.export_to_markdown())
        
        # Log the successful conversion
        add_to_log(target_path, log_file_path)
        logging.info(f"Successfully saved markdown file to {md_txt}")
        
    except Exception as e:
        logging.error(f"Error writing markdown file {md_txt}: {e}")
        return
    """Convert the file into markdown.

    Args:
        target_path (Path): Absolute path of the file to convert
        md_converter (_type_): Defined in the md, which may be either Docling or Markitdown.
    """
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(os.path.dirname(current_dir), 'logs')
    log_file_path = os.path.join(logs_dir, log_file_name)
    
    # Get the base directory and file name of the target path
    base_dir = os.path.dirname(target_path)
    base_name = os.path.basename(target_path)
    
    # Replace file extension to '.md'
    md_file_name = os.path.splitext(base_name)[0] + '.md'
    
    # Define the new root directory for markdown files (Datasets_md)
    root_md_dir = os.path.join(os.path.dirname(base_dir), 'Datasets_md')
    
    # Maintain the subfolder structure from the original target_path in 'Datasets_md'
    relative_path = os.path.relpath(base_dir, start=os.path.dirname(target_path))  # Relative path from 'Datasets'
    md_folder = os.path.join(root_md_dir, relative_path)  # Subfolder structure inside 'Datasets_md'
    
    # Full path for the markdown file in the 'Datasets_md' structure
    md_txt = os.path.join(md_folder, md_file_name)
    
    #* Primary check: Check if the file already exists in the log file
    if is_file_in_log(target_path, log_file_path):
        logging.info(f"File {target_path} already processed according to log file. Skipping conversion.")
        return
    
    #* Secondary check: Check if the markdown file already exists in the Datasets_md folder (Will remove later)
    expected_md_path = os.path.join(md_folder, md_file_name)
    print(expected_md_path)
    
    if os.path.exists(expected_md_path):
        logging.info(f"Markdown file {expected_md_path} already exists. Skipping conversion.")
        # Add to log file if it exists but wasn't logged
        add_to_log(target_path, log_file_path)
        return
    
    # Ensure the target subfolder exists inside 'Datasets_md'
    os.makedirs(md_folder, exist_ok=True)
    
    # Call converter
    converter = md_converter()
    
    # Convert and save the markdown content
    try:
        result = converter.convert(target_path)
    except Exception as e:
        logging.error(f"Error converting file {target_path}: {e}")
        return

    # Write the result to the markdown file
    try:
        with open(md_txt, 'w', encoding='utf-8') as md_file:
            md_file.write(result.document.export_to_markdown())
        
        # Log the successful conversion
        add_to_log(target_path, log_file_path)
        logging.info(f"Successfully saved markdown file to {md_txt}")
        
    except Exception as e:
        logging.error(f"Error writing markdown file {md_txt}: {e}")
        return

def extract(topic=None,subtopic=None,file=None):
    """Extracts the `Datasets` directory for all files using MarkitDown util. See the [MarkitDown repo](https://github.com/microsoft/markitdown/) for more info including
    the supported file formats.

    Args:
        topic (string, optional): Main topic folder. Defaults to `None`. The following options are available:
            - `ElectronicsEng` - References for the Electronics Engineering topic
            - `ESAT` - References for the Electronics Systems and Technologies topic
            - `GEAS` - References for the General Enginerring and Applied Sciences topic
            - `Mathematics` - References for the Mathematics topic
            - `Others` - Relevant documents (Table of Specifications, Explanation files, config files)
            - `Quizzes` - Sample quizzes the chatbot can refer to for formatting
            
        subtopic (string, optional): A subtopic under each topic. There are only a list of valid values per topic, which you can refer to the README.md to know more. Defaults to `None`.
        
        file (string, optional): If there is a specific file that you want to scrape. Note that this is not allowed to be filled if both topic and subtopic are not given. Defaults to `None`. 

    Returns:
        None: The `extract` function does not return anything, by itself. The description of this script does return and show the changes after running the `extract` function.
    """
    
    main_folder = os.path.abspath("../Datasets/")
    
    if topic is not None:
        main_folder += f"{topic}/"
    if subtopic is not None:
        main_folder += f"{subtopic}/"
        
    if not os.path.isdir(main_folder):
        logging.error(f"The path '{main_folder}' is not a valid directory.")
        return
    
    # If a specific file is provided
    if file is not None:
        target_path = os.path.join(main_folder, file)
        print(target_path)
        if os.path.isfile(target_path):
            #logging.debug(f"Extracting file: {os.path.abspath(target_path)}") # Commented out because the docling provides logging info by itself
            convert_md(target_path, DocumentConverter,check_path="../Datasets_md/")
            
        else:
            logging.error(f"File '{file}' not found in '{main_folder}'.")
        return  # Exit after printing the specific file
    
    # Otherwise, list all files inside subfolders only
    for dirpath, dirnames, filenames in os.walk(main_folder):
        if dirpath == os.path.abspath(main_folder):
            continue  # Skip the main folder itself
        for fname in filenames:
            file_path = os.path.join(dirpath, fname)
            logging.debug(f"Extracting file: {os.path.relpath(file_path)}")
            convert_md(file_path, DocumentConverter,check_path="../Datasets_md/")  # Changed from target_path to file_path

parser = argparse.ArgumentParser(
    prog="extract",
    description="""This is an extraction script that scrapes all the datasets inside the Datasets folder. The Datasets folder is organized per large topics of the ECE boards, with subjects inside
    major topics. Each files should be uniquely named for each large topic per subfolder since the results of the scraping are collected inside log files that will be checked ocassionally if a previous reference already exists.
    There is also an optional argument for specific files only to skip the checking of the whole directory itself."""
)

parser.add_argument(
    "-d", "--folder",
    nargs="+",  # One or more values
    metavar=("TOPIC", "SUBTOPIC"),
    help="Specify the topic and an optional subtopic (in order)."
)

parser.add_argument(
    "-f", "--file",
    nargs="+",
    metavar="FILE",
    help="Specific file(s) to extract (optional)."
)

parser.add_argument(
    "-e", "--extractor",
    metavar="EXTRACTOR",
    help="Extractor to use between `Docling` or `Markitdown`. Default is `Markitdown`."
)

parser.add_argument("-o", "--output", type=str, default=f"extract_{datetime.date.today()}.txt", help="Output file")
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

# parser.add_argument()
args = parser.parse_args()

# Set up logging to both console and file
setup_logging(os.path.abspath(f"../logs/{args.output}"))

# Validation logic
if args.folder:
    if len(args.folder) > 2:
        logging.error("--folder accepts at most two values: TOPIC [SUBTOPIC]")
        sys.exit(1)
    if len(args.folder) == 2 and not args.folder[0]:
        logging.error("Cannot specify a subtopic without a topic.")
        sys.exit(1)

topic = args.folder[0] if args.folder else None
subtopic = args.folder[1] if args.folder and len(args.folder) > 1 else None
files = args.file if args.file else [None]

# Redirect output to file
for file in files:
    extract(topic=topic, subtopic=subtopic, file=file, )
    
# To invoke script:
# python extract.py -d ElectronicsEng ACDC -o result.txt -v
