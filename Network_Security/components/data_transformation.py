import sys
import os
import numpy as np
import pandas as  pd

from sklearn.impute import KNNImputer
from sklearn.pipeline  import Pipeline 


from Network_Security.logger.logger import logging
from Network_Security.exception.exception import NetworkSecurityException

from Network_Security.constants.training_pipeline import (
    TARGET_COLUMN,
    DATA_TRANSFORMATION_IMPUTER_PARAMS
) 

from Network_Security.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact
)

from Network_Security.entity.config_entity import (
    DataTransformationConfig 
)

from Network_Security.utils.main_utils.utils import(
    save_numpy_array_data,
    save_object
)



class DataTransformation:
    def __init__(
            self,
            data_validation_artifact: DataValidationArtifact,
            data_transformation_config: DataTransformationConfig
    ):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config


            # logging.info(f"self. data validation artifact : {self.data_validation_artifact}\n\n")
            # logging.info(f"self data transformation config : {self.data_transformation_config}\n\n")

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:
        try:
            df=pd.read_csv(file_path)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    

    def get_data_transformer_object(self):
        try:
            params=DATA_TRANSFORMATION_IMPUTER_PARAMS
            
            logging.info(f"type of the params : {type(params)}")
            logging.info(f"imputer paramas : {params}")

            imputer=KNNImputer(**params)
            processor=Pipeline([
                ("knn_imputer",imputer)
            ])
            return processor

        except Exception as e:
            raise NetworkSecurityException(e,sys)




    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            valid_train_file_path=self.data_validation_artifact.valid_train_file_path

            valid_test_file_path=self.data_validation_artifact.valid_test_file_path

            # logging.info(f"train path : {valid_train_file_path}")

            # logging.info(f"type of train path : {type(valid_train_file_path)}")

            # logging.info(f"test path : {valid_test_file_path}")

            # logging.info(f"type of test path : {type(valid_test_file_path)}")

            train_df=DataTransformation.read_data(
                valid_train_file_path
            )

            test_df=DataTransformation.read_data(
                valid_test_file_path        
            )

            target_column=TARGET_COLUMN

            logging.info(f"train df columns : {train_df.columns}")

            logging.info(f"test df columns : {test_df.columns}")

            logging.info(f"tatget column : {target_column}")

            input_feature_train_df=train_df.drop(
                columns=[target_column],
                axis=1
            )
            target_feature_train_df=train_df[target_column]
            target_feature_train_df=target_feature_train_df.replace(-1,0)


            input_feature_test_df=test_df.drop(
                columns=[target_column],
                axis=1
            )
            target_feature_test_df=test_df[target_column]
            target_feature_test_df=target_feature_test_df.replace(-1,0)

            preprocessor=self.get_data_transformer_object()

            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_train=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test=preprocessor_object.transform(input_feature_test_df)

            train_arr=np.c_[transformed_input_train,np.array(target_feature_train_df)]
            test_arr=np.c_[transformed_input_test, np.array(target_feature_test_df)]


            save_numpy_array_data(
                self.data_transformation_config.transformed_train_file_path,
                train_arr
            )

            save_numpy_array_data(
                self.data_transformation_config.transformed_test_file_path,
                test_arr
            )

            save_object(
                self.data_transformation_config.transformed_object_file_path,
                preprocessor_object
            )

            save_object(
                file_path="final_model/preprocessor.pkl",
                obj=preprocessor_object
            )

            data_transformation_artifact_object=DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path
            )

            return data_transformation_artifact_object

            


        except Exception as e:
            raise NetworkSecurityException(e,sys)
    