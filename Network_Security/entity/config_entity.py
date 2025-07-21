from datetime import datetime
import  os
import sys

from Network_Security.constants import training_pipeline

'''

TARGET_COLUMN="Result"
PIPELINE_NAME="Network_Security"
ARTIFACT_DIR="Artifacts"
FILE_NAME="phisingData.csv"


TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"



DATA_INGESTION_COLLECTION_NAME:str="NETWORK_DATA"
DATA_INGESTION_DATABASE_NAME:str="NIKHIL"
DATA_INGESTION_DIR_NAME:str="DATA_INGESTION"
DATA_INGESTION_FEATURE_STORE_DIR:str="FEATURE_STORE"
DATA_INGESTION_INGESTED_DIR:str="INGESTED"
DATA_INGESTION_TRAIN_TEST_SPLIT:float=0.2

'''

# print(training_pipeline.ARTIFACT_DIR)
# print(training_pipeline.TARGET_COLUMN)




class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        self.timestamp=timestamp.strftime("%d_%m_%y_%Hh_%Mm_%Ss")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,self.timestamp)



class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_name=os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.FILE_NAME
        )
        self.training_file_path=os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path=os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME
       )
        self.train_test_split_ratio=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT
        self.collection_name=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name=training_pipeline.DATA_INGESTION_DATABASE_NAME


    def __str__(self):
        return (
            f"Data Ingestion Config:\n"
            f"  Ingestion Dir       : {self.data_ingestion_dir}\n"
            f"  Feature Store Path  : {self.feature_store_file_name}\n"
            f"  Training File Path  : {self.training_file_path}\n"
            f"  Testing File Path   : {self.testing_file_path}\n"
            f"  Split Ratio         : {self.train_test_split_ratio}\n"
            f"  Collection Name     : {self.collection_name}\n"
            f"  Database Name       : {self.database_name}"
        )

 
if __name__=="__main__":
    obj=DataIngestionConfig(TrainingPipelineConfig())
    print(obj)




