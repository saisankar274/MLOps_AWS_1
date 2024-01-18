import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]:[%(message)s]')

project_name = "ccnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for each_file in list_of_files:
    file_dir, file_name = os.path.split(Path(each_file))
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f"creating directory; {file_dir} for the file: {file_name}")
    
    if (not os.path.exists(file_name)) or (os.path.getsize(file_name) == 0):
        with open(each_file , "w") as f:
            pass
            logging.info(f"creating empty file: {each_file}")
    
    else:
        logging.info(f"{file_name} already exists")