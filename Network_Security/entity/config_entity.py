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
    


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_VALIDATION_DIR_NAME
        )
        self.valid_data_dir=os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_VALID_DIR
        )
        self.invalid_data_dir=os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_INVALID_DIR
        )
        self.valid_train_file_path=os.path.join(
            self.valid_data_dir,
            training_pipeline.TRAIN_FILE_NAME
        )
        self.valid_test_file_path=os.path.join(
            self.valid_data_dir,
            training_pipeline.TEST_FILE_NAME
        )
        self.invalid_train_file_path=os.path.join(
            self.invalid_data_dir,
            training_pipeline.TRAIN_FILE_NAME
        )
        self.invalid_test_file_path=os.path.join(
            self.invalid_data_dir,
            training_pipeline.TEST_FILE_NAME
        )
        self.drift_report_file_path=os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )

    def __str__(self):
        return (
            f"Data Validation Config:\n"
            f"Validation Directory: {self.data_validation_dir}\n"
            f"Valid Data Directory: {self.valid_data_dir}\n"
            f"Invalid Data Directory: {self.invalid_data_dir}\n"
            f"Valid Train File: {self.valid_train_file_path}\n"
            f"Valid Test File: {self.valid_test_file_path}\n"
            f"Invalid Train File: {self.invalid_train_file_path}\n"
            f"Invalid Test File: {self.invalid_test_file_path}\n"
            f"Drift Report File: {self.drift_report_file_path}"
        )

 



class DataTransformationConfig:
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME
        )
        self.transformed_train_file_path: str = os.path.join(
            self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"),
        )
        self.transformed_test_file_path: str = os.path.join(
            self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace("csv", "npy"),
        )
        self.transformed_object_file_path: str = os.path.join( 
            self.data_transformation_dir, 
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME,
        )
        



class ModelTrainerConfig:
    def __init__(
            self,
            training_pipeline_config:TrainingPipelineConfig
    ):
        self.model_trainer_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path:str=os.path.join(
            self.model_trainer_dir,
            training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,
            training_pipeline.MODEL_FILE_NAME
        )
        self.expected_accuracy:float=training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold=training_pipeline.MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD

        

 
# if __name__=="__main__":
#     obj=DataIngestionConfig(TrainingPipelineConfig())
#     print(obj)

#     obj=DataValidationConfig(TrainingPipelineConfig())
#     print(obj)



