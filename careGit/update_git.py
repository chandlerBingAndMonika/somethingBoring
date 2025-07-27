from careGit.check_upgrades import check_latest_version
from careGit.downloadGit import clone_latest_git_repo_gitpython
from pymongo.collection import Collection
from typing import List



from careDataBase import connect
from careDataBase.dataModel import Version_Packages


from careDataBase.update_data import update_data

def git_update_if_need(collection: Collection, package_list: List[Version_Packages]):
    filtered_packages: List[Version_Packages] = []
    for x in package_list:
        if x.is_web == False:
            filtered_packages.append(x)
    for package in filtered_packages:
        latest = check_latest_version(package.version, package.repo_url)
        if latest != package.version:
            clone_latest_git_repo_gitpython(package.repo_url, package.name, package.storage_path)
            update_data(collection, package.name, latest)

        

    
