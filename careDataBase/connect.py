from pymongo import MongoClient
import os
from dotenv import load_dotenv

# התחברות לשרת מרוחק של מונגו (MongoDB Atlas)



def connect_to_database():
    load_dotenv()  # טוען את משתני הסביבה מהקובץ .env
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise ValueError("MONGO_URI לא מוגדר בקובץ .env")
    careDB = os.getenv("DB_NAME", "careDB")  # שם ברירת מחדל למסד הנתונים
    client = MongoClient(mongo_uri)
    print("חיבור לשרת המרוחק:", mongo_uri)
    db = client[careDB]
    collection = db['packages']  # שם האוסף (collection) שבו נשמור את הנתונים
    print(f"התחברנו למסד הנתונים {careDB} ואוסף {collection.name}")
    try:
        client.admin.command('ping')  # בדיקת חיבור
        print("החיבור למסד הנתונים תקין.")
    except Exception as e:
        print("שגיאה בחיבור למסד הנתונים:", e)
        client.close()
        raise
    return client, collection
if __name__ == "__main__":
    client, collection = connect_to_database()
    # כאן אפשר להוסיף קוד נוסף לעבודה עם מסד הנתונים
    # לדוגמה, הוספת מסמך חדש לאוסף
    sample_document = {"name": "test", "value": 123}
    collection.insert_one(sample_document)
    print("מסמך נוסף בהצלחה:", sample_document)
    client.close()  # סגירת החיבור בסיום
    