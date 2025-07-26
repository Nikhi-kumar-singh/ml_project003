import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

from Network_Security.logger.logger import logging
from Network_Security.logger.logger import LOG_FILE_PATH
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.entity.config_entity import(
    DataIngestionConfig,
    TrainingPipelineConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)
from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import (
    DataValidation,
    DataValidationConfig,
    DataValidationArtifact
)  
from Network_Security.components.data_transformation import (
    DataTransformation
)
from Network_Security.components.model_trainer import ModelTrainer


if __name__=="__main__":
    try:
        os.system(f"code {LOG_FILE_PATH}")

        training_pipeline_config_obj=TrainingPipelineConfig()

        data_ingestion_config_obj=DataIngestionConfig(training_pipeline_config_obj)
        data_ingestion_obj=DataIngestion(data_ingestion_config_obj)
        data_ingestion_artifact_obj=data_ingestion_obj.initiate_data_ingestion()

        print(data_ingestion_artifact_obj) 
        logging.info(f"data ingestion artifact obj : {data_ingestion_artifact_obj}")

        data_validation_config_obj=DataValidationConfig(training_pipeline_config_obj) 
        data_validation_obj= DataValidation(
            data_ingestion_artifact=data_ingestion_artifact_obj,
            data_validation_config=data_validation_config_obj
        )
        data_validation_artifact_obj=data_validation_obj.initiate_data_validation()

        print(data_validation_artifact_obj)
        logging.info(f"data validation artifact : {data_validation_artifact_obj}")

        data_transformation_config_obj=DataTransformationConfig(
            training_pipeline_config_obj
        )
        
        data_transformation_object = DataTransformation(
            data_validation_artifact=data_validation_artifact_obj,
            data_transformation_config=data_transformation_config_obj
        )


        data_transformation_artifact_obj=data_transformation_object.initiate_data_transformation() 

        print(f"data transformation artifact : \n{data_transformation_object}")
        logging.info(f"data transformation artifact obj : {data_transformation_artifact_obj}")


        model_trainer_config_object=ModelTrainerConfig(
            training_pipeline_config=training_pipeline_config_obj
        )
        model_trainer_object=ModelTrainer(
            model_trainer_config=model_trainer_config_object,
            data_transformation_artifact=data_transformation_artifact_obj
        )
        model_trainer_artifact_object=model_trainer_object.initiate_model_trainer()

        logging.info(f"model trainer artifact object\n  {model_trainer_artifact_object}")

        '''
        after this step :
            run in terminal : mlflow ui
        '''

    except Exception as e:
        raise NetworkSecurityException(e,sys)