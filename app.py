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
from fastapi import (
    FastAPI, 
    File, 
    UploadFile,
    Request
)
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
from Network_Security.utils.ml_utils.model.estimator import NetworkModel



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



from fastapi.templating import Jinja2Templates
templates= Jinja2Templates(directory="./templates")



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
    



@app.post("/predict")
async def predict_route(request:Request,file:UploadFile=File(...)):
    try:
        input_file_path = "valid_data/input.csv"
        output_file_path = "valid_data/output.csv"
        preprocessor_path= "final_model/preprocessor.pkl"
        model_path= "final_model/model.pkl"

        df=pd.read_csv(input_file_path)
        preprocessor=load_object(preprocessor_path)
        model=load_object(model_path)

        network_model_object=NetworkModel(
            preprocessor=preprocessor,
            model=model
        )

        y_pred=network_model_object.predict(df)
        
        df["predicted_column"] = y_pred

        df.to_csv(
            output_file_path,
            index=False,
            header=True
        )

        table_html = df.to_html(classes="table table-striped")

        return templates.TemplateResponse(
            "table.html",
            {
                "request":request,
                "table":table_html
            }
        )

    except Exception as e:
        raise NetworkSecurityException(e,sys)


if __name__=="__main__":
    app_run(app,host="localhost",port=8000)