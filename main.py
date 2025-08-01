from careDataBase import connect
from careDataBase.dataModel import Version_Packages
from careDataBase.get_data import get_data, check_packages_for_updates
from careGit.update_git import git_update_if_need

from pymongo.collection import Collection

from careWeb.update_web import update_web_if_need


import schedule
import time


def main():
    schedule.every().day.at("11:27").do(update_every_day)

    while True:
        schedule.run_pending()
        time.sleep(60)


def update_every_day():
    # התחברות למסד הנתונים
    client, collection = connect.connect_to_database()


    # שליפת כל החבילות מהאוסף
    packages: Collection = get_data(collection)
    print(f"finding {len(packages)} packages in data base")
    git_update_if_need(collection, packages)
    update_web_if_need(collection, packages)


    # סגירת החיבור למסד הנתונים
    client.close()
if __name__ == "__main__":
    main()