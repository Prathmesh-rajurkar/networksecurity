from pymongo.mongo_client import MongoClient
from collections.abc import MutableMapping

uri = "mongodb+srv://prathmeshrajurkar199:cQD9omBoqu4JC0Id@cluster0.cvulq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)