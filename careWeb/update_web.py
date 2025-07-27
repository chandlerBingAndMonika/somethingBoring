from careGit.check_upgrades import check_latest_version
from careGit.downloadGit import clone_latest_git_repo_gitpython
from careWeb.check_releases import get_stable_release
from pymongo.collection import Collection
from typing import List

from careDataBase.dataModel import Version_Packages


from careDataBase.update_data import update_data
from careWeb.check_upgrades import get_link_download
from careWeb.download_web import download_package

def update_web_if_need(collection: Collection, package_list: List[Version_Packages]):
    filtered_packages: List[Version_Packages] = []
    for x in package_list:
        if x.is_web == True:
            filtered_packages.append(x)
    for package in filtered_packages:
        latest = get_stable_release(package.web_site_to_version)
        if latest == package.version:
            continue
        print(package.repo_url)
        if package.is_direct == True:
            download_url = package.repo_url
        else:
            download_url = str(get_link_download(package.repo_url))
        is_download = download_package(download_url, package.storage_path, package.name)
        if is_download == 0:
            update_data(collection, package.name, latest)

        

    
