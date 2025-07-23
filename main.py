from careDataBase import connect
from careDataBase.dataModel import Version_Package
from careDataBase.get_data import get_data, check_packages_for_updates
from careGit.update_git import update_if_need

from pymongo.collection import Collection

def main():
    # התחברות למסד הנתונים
    client, collection = connect.connect_to_database()

    # # יצירת אובייקט חדש של Version_Pacage
    # package = Version_Package(
    # name="example_package",
    # repo_url="BurntSushi",
    # storage_path="/packages/mypackage",
    # version="1.0.0"
    # )

    # שמירה למסד הנתונים
    # package.save()
    # print("the package save succesfull", package.name)

    # שליפת כל החבילות מהאוסף
    packages: Collection = get_data(collection)
    print(f"finding {len(packages)} packages in data base")
    update_if_need(collection, packages)

    # סגירת החיבור למסד הנתונים
    client.close()
if __name__ == "__main__":
    main()