import os
import requests
from dotenv import load_dotenv

def download_package(url, path, name):
    load_dotenv()

    try:
        # הנתיב לתיקייה שבה יישמר הקובץ
        target_dir = os.getenv("TARGER_REPO", path)
        os.makedirs(target_dir, exist_ok=True)  # נוודא שהתיקייה קיימת

        # הנתיב המלא לקובץ
        file_path = os.path.join(target_dir, name)

        # אם הקובץ כבר קיים – נמחק אותו
        if os.path.exists(file_path):
            os.remove(file_path)

        # שליחת הבקשה
        response = requests.get(url)

        if response.status_code == 200:
            # כתיבת הקובץ לדיסק
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print(f"הקובץ הורד בהצלחה אל: {file_path}")
            return 0
        else:
            print(f"שגיאה: סטטוס לא תקין ({response.status_code}) מהשרת.")
            return 1

    except Exception as e:
        print(f"שגיאה בהורדה: {e}")
        return 1
