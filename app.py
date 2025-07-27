import os
import sys
import pandas as pd
import numpy as np


import certifi
ca=certifi.where()

from dotenv import load_dotenv
load_dotenv()


import pymongo
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse



from Network_Security.logger.logger import logging
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.pipeline.training_pipeline import TrainingPipeline

from Network_Security.utils.main_utils.utils import (
    load_object
)

from Network_Security.constants.training_pipeline import (
    DATA_INGESTION_COLLECTION_NAME,
    DATA_INGESTION_DATABASE_NAME
)



mongo_db_url=os.getenv("MONGO_DB_URL")
print(mongo_db_url)


client=pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
database=client[DATA_INGESTION_DATABASE_NAME]
collection=database[DATA_INGESTION_COLLECTION_NAME]

app=FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")




@app.get("/train")
async def train_route():
    try:
        train_pipeline_object=TrainingPipeline()
        train_pipeline_object.run_training_pipeline()

        return Response("training is successful")

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    



if __name__=="__main__":
    app_run(app,host="localhost",port=8000)