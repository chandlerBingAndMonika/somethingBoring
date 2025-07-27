import shutil
import stat
import os

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