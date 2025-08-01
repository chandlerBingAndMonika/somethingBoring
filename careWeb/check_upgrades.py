import requests
from bs4 import BeautifulSoup

def get_link_download(url: str):

    # שליחה של בקשה לדף
    response = requests.get(url)
    false_links = get_valid_download_links(url)

    # אם הבקשה הצליחה
    if response.status_code == 200:
        print ("200")
        # ניתוח ה-HTML בעזרת BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # מציאת כל הקישורים על הדף (למשל, קישורים להורדה)
        download_links = soup.find_all('a', href=True)
        filtered_links = []

        for link in download_links:
            href = link['href']
            # נבדוק אם מילה אסורה מהרשימה קיימת בקישור
            if not any(bad in href for bad in false_links):
                filtered_links.append(href)
        for link in filtered_links:
            if check_file_type(link['href']):
                download_url = link['href']
                # אם ה-URL הוא קישור יחסי, יש להוסיף את הבסיס (base URL)
                if not download_url.startswith('http'):
                    download_url = get_base_url(url) + download_url
                print("download file is ", download_url)
                return download_url
    else:
        print(f'בקשה לדף נכשלה, קוד סטטוס: {response.status_code}')
        return ""



def get_valid_download_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    # מחפש גם <a> וגם <button> (למרות ש-buttons לא תמיד מכילים href)
    elements = soup.find_all(['a', 'button'])

    for el in elements:
        text = el.get_text(strip=True).lower()
        
        # בודק שהתוכן כולל 'download' ולא כולל '32'
        if 'download' in text and '32' not in text:
            # אם זו תגית <a> עם href – נוסיף את הקישור
            if el.name == 'a' and el.has_attr('href'):
                links.append(el['href'])
            # אם זה <button> ויש בתוכו <a href=...> כלשהו
            inner_links = el.find_all('a', href=True)
            for inner in inner_links:
                links.append(inner['href'])

    return links


def check_file_type(url):
    url = str(url)
    # בדיקת אם כתובת ה-URL מכילה אחד מהתנאים
    file_types = ['.exe', '.zip']
    
    # מבצע בדיקה אם ה-URL מכיל את אחד מהסוגים
    if any(file_type in url.lower() for file_type in file_types):
        print("its true " + url)
        return True
    
    return False

def get_base_url(url: str):
    end_index = -1
    if '.com' in url:
        end_index = url.find('.com') + len('.com/')
    elif '.org' in url:
        end_index = url.find('.org') + len('.org/')

    if end_index != -1:
        return url[:end_index]
    else:
        return url  # אם אין .com או .org נחזיר את כל המחרוזת כמו שהיא





