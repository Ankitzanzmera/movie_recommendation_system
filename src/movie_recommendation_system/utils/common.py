import os,sys
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from pathlib import Path
from movie_recommendation_system.utils.exception import CustomException
from typing import Any

# @ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    try:
        with open(filepath,"r") as yaml_file:   
            content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml is empty")
    except Exception as e:
        raise CustomException(e,sys)
    
# @ensure_annotations 
def create_directories(path_to_directory) -> None:
    for path in path_to_directory:
        os.makedirs(path,exist_ok= True)    
