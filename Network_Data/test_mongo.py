import os
import sys
import json
import certifi
from dotenv import load_dotenv

load_dotenv()

mongo_atlas_user_name=os.getenv("MONGO_ATLAS_USER_NAME")
mongo_atlas_password=os.getenv("MONGO_ATLAS_PASSWORD")
mongo_atlas_cluster_name=os.getenv("MONGO_ATLAS_CLUSTER_NAME")
MONGO_DB_URL1=os.getenv("MONGO_DB_URL")

MONGO_DB_URL2=f"mongodb+srv://{mongo_atlas_user_name}:{mongo_atlas_password}@{mongo_atlas_cluster_name}.n1vzevj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# print(MONGO_DB_URL1)
# print(MONGO_DB_URL2)

ca=certifi.where()