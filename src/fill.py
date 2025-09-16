# This is a simpel function to add placeholder text files to each directory in Datasets 

import os
import subprocess

for root, dirs, files in os.walk('Datasets_md') :
    for fir in dirs:
        file_name = f"{root}/{fir}/{fir}.txt"
        print(file_name)
        subprocess.run(['touch',file_name])
