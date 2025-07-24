import pandas as pd
import numpy as np
import os
import sys

# Kolmogorov–Smirnov (K–S) Test 
from scipy.stats import ks_2samp


from Network_Security.entity.artifact_entity import(
    DataIngestionArtifact,
    DataValidationArtifact
)

from Network_Security.entity.config_entity import (
    DataIngestionConfig,
    training_pipeline,
    DataValidationConfig
)

from Network_Security.utils.main_utils.utils import (
    read_yaml_file,
    write_yaml_file
)

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

from Network_Security.constants.training_pipeline import SCHEMA_FILE_PATH
 



class DataValidation:
    def __init__(
            self,
            data_ingestion_artifact:DataIngestionArtifact,
            data_validation_config:DataValidationConfig
    ):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    @staticmethod
    def read_data(file_path):
        try:
            df=pd.read_csv(file_path)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)



    def validate_number_of_columns(self,dataframe:pd.DataFrame):
        try:
            number_of_columns=len(self._schema_config)
            # logging.info(f"schema config file : {self._schema_config}")

            if len(dataframe.columns)==number_of_columns:
                return True
            else :
                return False

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        



    def detect_dataset_drift(self,base_df,current_df,threshold=0.5):
        try:
            status=True
            report={}
            for  column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_same_dist=ks_2samp(d1,d2)
                if threshold <= is_same_dist.pvalue:
                    is_found=False
                else:
                    is_found=True
                    status=False
                report.update({column:{
                    "p_value":float(is_same_dist.pvalue),
                    "drift_status":is_found
                }})
            drift_report_file_path=self.data_validation_config.drift_report_file_path

            dir_path=os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(
                file_path=drift_report_file_path,
                content=report,
                replace=True    
            )

        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_data_validation(self):
        try:
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)

            # logging.info(f"type of train_dataframe : {train_dataframe}")
            # logging.info(f"type of test_dataframe : {test_dataframe}")

            train_data_status=self.validate_number_of_columns(train_dataframe)
            status_message=""
            if train_data_status:
                status_message=f"train file contains all the columns"
            else :
                status_messageg=f"train file not contain all the columns"

            status=self.detect_dataset_drift(
                base_df=train_dataframe,
                current_df=test_dataframe
            )

            dir_path=os.path.dirname(self.data_validation_config.valid_test_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            if status : 
                train_dataframe.to_csv(
                    self.data_validation_config.valid_train_file_path,
                    index=False,
                    header=True
                )

                test_dataframe.to_csv(
                    self.data_validation_config.valid_test_file_path,
                    header=True,
                    index=False
                )


            data_validation_artifact=DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_ingestion_artifact.train_file_path,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )


            return data_validation_artifact
             
        except Exception as e:
            raise NetworkSecurityException(e,sys)