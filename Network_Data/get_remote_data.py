from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

user_name="nikhilkumarsingh5872"
password="mVxxZZ744EMlU5a8"

uri = f"mongodb+srv://{user_name}:{password}@cluster0.n1vzevj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# print(f"uri : {uri}")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)