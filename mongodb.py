# MongoDB setup
from pymongo import MongoClient
import config

client = MongoClient(f"mongodb+srv://{config.MONGO_USER}:{config.MONGO_PASS}@cluster0.jycdcnt.mongodb.net/{config.MONGO_DBNAME}")

db = client[config.MONGO_DBNAME]
collection = db[config.MONGO_COL]