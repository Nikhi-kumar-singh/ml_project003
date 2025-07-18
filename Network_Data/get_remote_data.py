from dotenv import load_dotenv
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MONGO_ATLAS_USER_NAME")
password = os.getenv("MONGO_ATLAS_PASSWORD")
cluster = os.getenv("MONGO_ATLAS_CLUSTER_NAME")
env_uri=os.getenv("MONGO_DB_URL")

uri = f"mongodb+srv://{user}:{password}@{cluster}.n1vzevj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client1 = MongoClient(env_uri)
client2 = MongoClient(uri)


# Test connection
try:
    client1.admin.command('ping')
    print("uri1 Connected successfully!")
    client2.admin.command('ping')
    print("uri2 Connected successfully!")
except Exception as e:
    print("Connection failed:", e)
