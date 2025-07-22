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