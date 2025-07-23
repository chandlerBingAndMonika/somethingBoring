import careDataBase.connect
from pymongo.collection import Collection

def update_data(collection: Collection, name: str, version: str):

    """
    פונקציה לעדכון המידע בבסיס הנתונים על פי שם.
    
    :param collection: האוסף שבו נשמרים הנתונים
    :param name: השם של התיעוד שנרצה לעדכן
    :param version: הגרסה החדשה לעדכון
    """
    # חיפוש של תיעוד לפי שם
    care_version = collection.find_one({"name": name})

    if care_version:
        # אם מצאנו את התיעוד, נבצע עדכון
        updated_document = {
            "version": version
        }
        
        # עדכון התיעוד ב-DB
        result = collection.update_one({"name": name}, {"$set": updated_document})
        
        if result.modified_count > 0:
            print(f"the update completed succesfull{name}")
        else:
            print(f"the upgrade of {name}, may failed")
    else:
        print ("there is no value with this name")






