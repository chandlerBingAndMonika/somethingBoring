from careGit.check_upgrades import check_latest_version
from careDataBase.dataModel import Version_Packages

from typing import List
from pymongo.collection import Collection

def get_data(collection: Collection) -> List[Version_Packages]:
    all_packages = collection.find()  # שליפת כל החבילות מהאוסף
    packages_list = []
    for package in all_packages:
        # מסירים שדות שלא קיימים במודל
        package.pop('_id', None)
        package.pop('value', None)
        # המרת המילון לאובייקט של Version_Package
        packages_list.append(Version_Packages(**package))

    print(f"Found {len(packages_list)} packages in the database")
    for package in all_packages:
        print(f"Package: {package.name}, Version: {package.version}, Repo: {package.repo_url}")
    return packages_list


def check_packages_for_updates(packages: List[Version_Packages]) -> List[Version_Packages]:
    updated_packages = []
    for package in packages:
        print(f"Package: {package.name}, Version: {package.version}, Repo: {package.repo_url}")
    for package in packages:
        if not check_latest_version(str(package.version), str(package.repo_url)):
            print(f"there is a new version {package.name} (version {package.version})")
            updated_packages.append(package)
        else:
            print(f"package {package.name} upgrade to version {package.version}")
    return updated_packages
