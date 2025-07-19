import sys
import os
import json
from dotenv import load_dotenv
load_dotenv()
import certifi
import pandas as pd
import numpy as np
import pymongo
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging



MONGO_DB_URL=os.getenv("MONGO_DB_URL")
# print(f"mongo atlas url : {MONGO_DB_URL}")
ca=certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def csv_to_json_convertor(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            records=list(json.loads(df.T.to_json(orient="records")))
            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        


    def insert_data_into_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records


            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records )
            return len(self.records)


        except Exception as e:
            raise NetworkSecurityException(e,sys)








if __name__=="__main__":
    FILE_PATH="E:/GitHubFIles/ML_project003/Network_Data/phisingData.csv"
    DATABASE="NIKHIL"
    COLLECTION="NETWORK_DATA"
    obj=NetworkDataExtract()
    RECORDS=obj.csv_to_json_convertor(FILE_PATH)
    print(RECORDS)
    number_of_records=obj.insert_data_into_mongo(
        records=RECORDS,
        database=DATABASE,
        collection=COLLECTION
    )

    print(f"number of records : {number_of_records}")

