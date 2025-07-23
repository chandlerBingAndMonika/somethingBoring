from careGit.check_upgrades import check_latest_version
from careGit.downloadGit import clone_latest_git_repo_gitpython
from pymongo.collection import Collection
from typing import List



from careDataBase import connect
from careDataBase.dataModel import Version_Package


from careDataBase.update_data import update_data

def update_if_need(collection: Collection, package_list: List[Version_Package]):
    for f in package_list:
        print(f.is_web)
    filtered_packages: List[Version_Package] = []
    for x in package_list:
        if x.is_web == False:
            filtered_packages.append(x)
    for package in filtered_packages:
        print("fghj")
        latest = check_latest_version(package.version, package.repo_url)
        if latest != package.version:
            clone_latest_git_repo_gitpython(package.repo_url, package.name, package.storage_path)
            update_data(collection, package.name, latest)

        

    
