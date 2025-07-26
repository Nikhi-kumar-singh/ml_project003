import os,sys

from Network_Security.logger.logger import logging
from Network_Security.exception.exception import NetworkSecurityException

from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation
from Network_Security.components.data_transformation import DataTransformation
from Network_Security.components.model_trainer import ModelTrainer


from Network_Security.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from Network_Security.entity.artifact_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ClassificationMetricArtifact,
    ModelTrainerArtifact
)


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config_object=TrainingPipelineConfig()


    def start_data_ingestion(self):
        try:
            self.data_ingestion_config_object=DataIngestionConfig(self.training_pipeline_config_object)

            self.data_ingestion_object=DataIngestion(self.data_ingestion_config_object)

            self.data_ingestion_artifact_object=self.data_ingestion_object.initiate_data_ingestion()

            logging.info(self.data_ingestion_artifact_object)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def start_data_validation(self):
        try:
            self.data_validation_config_object=DataValidationConfig(self.training_pipeline_config_object)

            self.data_validation_object=DataValidation(
                data_ingestion_artifact=self.data_ingestion_artifact_object,
                data_validation_config=self.data_validation_config_object
            )
            self.data_validation_artifact_object=self.data_validation_object.initiate_data_validation()

            logging.info(self.data_validation_artifact_object)

        except Exception as e:
            raise  NetworkSecurityException(e,sys)


    def start_data_transformation(self):
        try:
            self.data_transformation_config_object=DataTransformationConfig(
                self.training_pipeline_config_object
            )
            
            self.data_transformation_object = DataTransformation(
                data_validation_artifact=self.data_validation_artifact_object,
                data_transformation_config=self.data_transformation_config_object
            )

            self.data_transformation_artifact_object=self.data_transformation_object.initiate_data_transformation() 
            
            logging.info(self.data_transformation_artifact_object)


        except Exception as e:
            raise  NetworkSecurityException(e,sys)



    def start_model_training(self):
        try:
            self.model_trainer_config_object=ModelTrainerConfig(
                training_pipeline_config=self.training_pipeline_config_object
            )

            self.model_trainer_object=ModelTrainer(
                model_trainer_config=self.model_trainer_config_object,
                data_transformation_artifact=self.data_transformation_artifact_object
            )
            self.model_trainer_artifact_object=self.model_trainer_object.initiate_model_trainer()

            logging.info(self.model_trainer_artifact_object)

        except Exception as e:
            raise  NetworkSecurityException(e,sys)



    def run_training_pipeline(self):
        self.start_data_ingestion()
        self.start_data_validation()
        self.start_data_transformation()
        self.start_model_training()




if __name__=="__main__":
    obj=TrainingPipeline()
    obj.run_training_pipeline()


