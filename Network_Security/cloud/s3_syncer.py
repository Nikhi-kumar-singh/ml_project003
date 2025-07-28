import os
import sys
from Network_Security.exception.exception import NetworkSecurityException


class S3Sync:
    def sync_folder_to_s3(
        self,
        folder,
        aws_bucket_url
    ):
        try:
            command=f"aws s3 sync {self.folder} {aws_bucket_url}"
            os.system(command)

        except Exception as e:
            raise NetworkSecurityException(e,sys)




    def sync_folder_from_s3(
        self,
        folder,
        aws_bucket_url
    ):
        try:
            command=f"aws s3 sync {aws_bucket_url} {self.folder}"
            os.system(command)

        except Exception as e:
            raise NetworkSecurityException(e,sys)