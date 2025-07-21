import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys
# FILE_PATH="Network_Data/phisingData.csv"

# df=pd.read_csv(FILE_PATH)
# print(df.columns)

# print(datetime.now())

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.entity.config_entity import(
    DataIngestionConfig,
    TrainingPipelineConfig
)
from Network_Security.components.data_ingestion import DataIngestion




if __name__=="__main__":
    try:
        training_pipeline_config_obj=TrainingPipelineConfig()
        data_ingestion_config_obj=DataIngestionConfig(training_pipeline_config_obj)
        data_ingestion=DataIngestion(data_ingestion_config_obj)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)