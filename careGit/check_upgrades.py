import requests
import sys

def check_latest_version(current_version: str, repo_url: str):
    # הוצאת שם הרפוזיטורי מכתובת GitHub

    parts = repo_url.strip("/").split("/")
    if len(parts) < 2:
        print("error: the url is not valid")
        return

    owner, repo = parts[-2], parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    print(api_url)

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release.get("tag_name", "").lstrip("v")

        print(f"this version is the latest in github: {latest_version}")
        print(f"your version is: {current_version}")

        return latest_version

    except requests.exceptions.RequestException as e:
        print("an error in GitHub:", e)


