from urllib.parse import quote_plus
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_ADD = "localhost:27017"
MONGODB_U = "root"
MONGODB_P = "vtd@123!@#"

mongodb_uri = "mongodb://%s:%s@%s/?authSource=admin" % (
        quote_plus(MONGODB_U), quote_plus(MONGODB_P),quote_plus(MONGODB_ADD))

# mongodb_uri = "mongodb://%s" % (quote_plus(MONGODB_ADD))

# mongo_client = MongoClient(mongodb_uri)
mongo_client = AsyncIOMotorClient(mongodb_uri)

print(mongo_client.list_database_names())