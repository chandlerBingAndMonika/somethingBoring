from mongoengine import connect as mongoengine_connect
import os
from dotenv import load_dotenv
from pymongo import MongoClient

def connect_to_database():
    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME", "careDB")
    collection_name = os.getenv("DBCOLLECTION", "version__package")

    try:
        # התחברות עם pymongo
        client = MongoClient(mongo_uri)
        client.admin.command('ping')  # בדיקת חיבור
        print(f"Connected successfully to MongoDB server: {mongo_uri}")

        db = client[db_name]
        collection = db[collection_name]
        print(f"Using database '{db_name}' and collection '{collection.name}'")

        # התחברות ל־mongoengine
        mongoengine_connect(
            db=db_name,
            host=mongo_uri,
            alias='default'
        )

        return client, collection
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        raise
