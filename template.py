from fileinput import filename
import os
from pathlib import Path
import logging
from attr import field

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s: ')

package_name = "deepclassifier"

list_of_files = [".github/workflows/.gitkeep",
                f"src/{package_name}/__init__.py",
                f"src/{package_name}/components/__init__.py",
                f"src/{package_name}/util/__init__.py",
                f"src/{package_name}/config/__init__.py",
                f"src/{package_name}/pipeline/__init__.py",
                f"src/{package_name}/entity/__init__.py",
                f"src/{package_name}/constants/__init__.py",
                "configs/config.yaml",
                "dvc.yaml",
                "param.yaml",
                "init_setup.sh",
                "requirements.txt",
                "requirements_dev.txt",
                "setup.py",
                "setup.cfg",
                "pyproject.toml",
                "tox.ini",
                "research/trials.ipynb"]


for filepath  in list_of_files:
    filepath = Path(filepath)
    filedir, file_name = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=False)
        logging.info(f"Creating directory:{filedir} for file:{file_name}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating directory: {filedir}")
    
    else:
        logging.info(f"File already exists")

    