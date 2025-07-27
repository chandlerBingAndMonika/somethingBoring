import requests
from bs4 import BeautifulSoup

def get_stable_release(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # חיפוש כל שורות הטבלה
    for tr in soup.find_all('tr'):
        th = tr.find('th')
        td = tr.find('td')
        if th and td and 'release' in th.text.lower() and 'stable' in th.text.lower():
            return extract_numeric_prefix(td.text.strip())
    return "not found"


def extract_numeric_prefix(s):
    result = ''
    for char in s:
        if char.isdigit() or char == '.':
            result += char
        else:
            break
    return result


