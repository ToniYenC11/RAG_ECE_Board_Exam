import os
import subprocess

for root, dirs, files in os.walk('Datasets') :
    for fir in dirs:
        file_name = f"{root}/{fir}/{fir}.txt"
        print(file_name)
        subprocess.run(['touch',file_name])
