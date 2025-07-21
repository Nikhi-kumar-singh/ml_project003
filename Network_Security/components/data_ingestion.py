import os
import sys
from pymongo import MongoClient
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging
from  Network_Security.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig
)
from Network_Security.entity.artifact_entity import DataIngestionArtifact


from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL=os.getenv("MONGO_DB_URL")
# print(f"{MONGO_DB_URL}")

class DataIngestion:
    def __init__(self,data_ingestion_config):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def export_collection_as_dataframe(self):
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop("_id",axis=1,inplace=True)
            df.replace({"na":np.nan},inplace=True)

            return df

        except Exception as e:
            raise NetworkSecurityException(e,sys)  


    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_name
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
                raise NetworkSecurityException(e,sys)


    def split_data_into_feature_store(self,df:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(
                df,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=143
            )

            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path,exist_ok=True)

            train_set.to_csv(
                self.data_ingestion_config.training_file_path,index=False,
                header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False,
                header=True
            )

        except Exception as e:
            raise NetworkSecurityException(e,sys)




    def initiate_data_ingestion(self):
        try:
            df=self.export_collection_as_dataframe() 
            df=self.export_data_into_feature_store(df)
            self.split_data_into_feature_store(df)
            data_ingestion_artifact=DataIngestionArtifact(
                self.data_ingestion_config.training_file_path,
                self.data_ingestion_config.testing_file_path
            )       
            return data_ingestion_artifact


        except Exception as e:
            raise NetworkSecurityException(e,sys)