import pandas as py
import numpy as np
import os
import sys
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

from Network_Security.utils.main_utils.utils import read_yaml_file

from exception.exception import NetworkSecurityException
from logger.logger import logging

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
