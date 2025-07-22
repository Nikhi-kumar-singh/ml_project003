import os,sys
import pandas as pd
import numpy as np
import yaml
import dill
import pickle


from Network_Security.logger.logger import logging
from Network_Security.exception.exception import NetworkSecurityException


def read_yaml_file(file_path:str) -> dict :
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def write_yaml_file(file_path:str,content:object,replace:bool=False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"w") as yaml_file:
            yaml.dump(content,yaml_file)

    except Exception as e:
        raise NetworkSecurityException(e,sys)