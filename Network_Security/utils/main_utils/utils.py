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
    



def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as array_file:
            np.save(array_file,array)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    



def save_object(file_path:str,obj:object):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path)
        
        with open(file_path,"wb") as obj_file:
            pickle.dump(obj,obj_file)

    except Exception as e:
        raise NetworkSecurityException(e,sys)