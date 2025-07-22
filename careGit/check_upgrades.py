import requests
import sys

def check_latest_version(current_version: str, repo_url: str):
    # הוצאת שם הרפוזיטורי מכתובת GitHub

    parts = repo_url.strip("/").split("/")
    if len(parts) < 2:
        print("שגיאה: לא הצלחתי להבין את שם הרפוזיטורי")
        return

    owner, repo = parts[-2], parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    print(api_url)

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release.get("tag_name", "").lstrip("v")

        print(f"הגרסה האחרונה ב־GitHub היא: {latest_version}")
        print(f"הגרסה שלך: {current_version}")

        if current_version == latest_version:
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print("שגיאה בשליפה מ־GitHub:", e)

# --- דוגמה להרצה ---
if __name__ == "__main__":
    current = input("הכנס את הגרסה שלך (למשל: 9.52): ").strip()
    repo = input("הכנס את כתובת ה־GitHub של הרפוזיטורי: ").strip()
    if check_latest_version(current, repo):
        print("הגרסה שלך מעודכנת.")
    else:
        print("יש גרסה חדשה זמינה.")
        sys.exit(1)
