# This is a simple function to add placeholder text files to each directory in Datasets 

import os
import subprocess

def process_placeholder_files(key):
    for root, dirs, files in os.walk('../Datasets/') :
        for fir in dirs:
            file_name = f"{root}/{fir}/{fir}.txt"
            if key == 'add':
                subprocess.run(['touch',file_name])
            elif key == 'remove':
                if os.path.exists(file_name):
                    os.remove(file_name)
process_placeholder_files('remove')  