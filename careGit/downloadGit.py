from git import Repo
import tempfile
from dotenv import load_dotenv
import os
import shutil
import stat
from care_folder.delete import unlock_and_delete



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
    






