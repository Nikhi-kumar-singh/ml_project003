import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.entity.config_entity import(
    DataIngestionConfig,
    TrainingPipelineConfig
)
from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import (
    DataValidation,
    DataValidationConfig
)  



if __name__=="__main__":
    try:
        training_pipeline_config_obj=TrainingPipelineConfig()

        data_ingestion_config_obj=DataIngestionConfig(training_pipeline_config_obj)
        data_ingestion_obj=DataIngestion(data_ingestion_config_obj)
        data_ingestion_artifact_obj=data_ingestion_obj.initiate_data_ingestion()

        print(data_ingestion_artifact_obj) 


        data_validation_config_obj=DataValidationConfig(training_pipeline_config_obj) 
        data_validation_obj= DataValidation(
            data_ingestion_artifact=data_ingestion_artifact_obj,
            data_validation_config=data_validation_config_obj
        )
        data_validation_artifact_obj=data_validation_obj.initiate_data_validation()

        print(data_validation_artifact_obj)


    except Exception as e:
        raise NetworkSecurityException(e,sys)