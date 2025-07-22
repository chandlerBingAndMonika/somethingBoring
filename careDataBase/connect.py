from pymongo import MongoClient

# התחברות לשרת מרוחק של מונגו (MongoDB Atlas)
client = MongoClient("mongodb+srv://chandlerandmonikathe1:aooXBxyjqel6oxhH@cluster0.xdzmbiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['careDB']
collection = db['patients']
collection.insert_one({"name": "ישראל ישראלי", "age": 30})

try:
    # ננסה לשלוף את שמות המסדים כדי לבדוק חיבור
    client.server_info()
    print("התחברת בהצלחה לשרת המרוחק!")

    # שליפת הרשומה שהכנסנו לדאטה בייס
    patient = collection.find_one({"name": "ישראל ישראלי", "age": 30})
    print("הרשומה שנשמרה בדאטה בייס:", patient)

except Exception as e:
    print("החיבור לשרת נכשל:", e)