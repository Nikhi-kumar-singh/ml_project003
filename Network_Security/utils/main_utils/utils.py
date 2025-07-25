import os,sys
import pandas as pd
import numpy as np
import yaml
import dill
import pickle


from Network_Security.logger.logger import logging
from Network_Security.exception.exception import NetworkSecurityException



from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score



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
    

def load_numpy_array_data(file_path):
    try:
        if not os.path.exists(file_path):
            raise Exception(f"the file {file_path} does not exist")
        
        with open(file_path,"rb") as array_file:
            array_obj=np.load(array_file)
            return array_obj

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
    



def load_object(file_path: str):
    try:
        if not os.path.exists(file_path):
            raise Exception(f"the file {file_path} does not exist.")
        
        with  open(file_path,"rb") as obj_file:
            obj=pickle.load(obj_file)
            return obj

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    




def evaluate_models(
    x_train,
    y_train,
    x_test,
    y_test,
    models,
    params
):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            param=list(params.values())[i]

            processor=GridSearchCV(
                estimator=model,
                param_grid=param,
                n_jobs=-1,
                cv=3
            )

            processor.fit(x_train,y_train)
            model.set_params(**processor.best_params_)
            model.fit(x_train,y_train)

            y_train_pred=model.predict(x_train)
            y_test_pred=model.predict(x_test)

            train_model_score=r2_score(
                y_train,
                y_train_pred
            )

            test_model_score=r2_score(
                y_test,
                y_test_pred
            )


            report[list(models.keys())[i]]={
                "score":test_model_score,
                "params":param
            }

        
        return report

    except Exception as e:
        raise NetworkSecurityException(e,sys)