import bleach
from bs4 import BeautifulSoup
import requests

url = "https://www.nairaland.com/6147649/court-awards-n50-million-against"
html = requests.get(url)
soup = BeautifulSoup(html.content, features="html.parser")
allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike', 'strong',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']

allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }

    

a=bleach.clean(soup.prettify(),tags=allowed_tags,attributes=allowed_attrs,strip=True)

#tree = BeautifulSoup(a, "lxml")
print( str(a)) 
