from git import Repo
import tempfile
from dotenv import load_dotenv
import os
import shutil
import stat



def clone_latest_git_repo_gitpython(uri: str, name: str, target_dir=None):
    load_dotenv()
    base_url = "https://github.com/"
    target_dir = os.getenv("TARGET_REPO")
    target_dir += "/" + name
    uri = str(base_url) + uri
    if target_dir is None:
        target_dir = tempfile.mkdtemp()

    unlock_and_delete(target_dir)

    try:
        Repo.clone_from(uri, target_dir, depth=1)
        print(f"הריפוזיטורי שוכפל ל- {target_dir}")
        return target_dir
    except Exception as e:
        print(f"שגיאה בשכפול: {e}")
        return None
    


def unlock_and_delete(folder_path):
    """
    Attempts to unlock and delete files that are locked before removing the entire directory.
    """
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                # Unlock the file (change its permissions to make it writable)
                os.chmod(file_path, stat.S_IWRITE)
                os.remove(file_path)  # Remove the file
                print(f"File {file_path} deleted successfully.")
            except PermissionError:
                print(f"Permission denied, cannot delete the file {file_path}.")
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)  # Remove empty directories
                print(f"Directory {dir_path} deleted successfully.")
            except PermissionError:
                print(f"Permission denied, cannot delete the directory {dir_path}.")

    try:
        shutil.rmtree(folder_path)  # Remove the directory itself
        print(f"Directory {folder_path} deleted successfully.")
    except Exception as e:
        print(f"Error occurred while deleting the directory: {e}")




