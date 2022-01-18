import requests
from bs4 import BeautifulSoup
import bleach
import markdown
import bleach
from bleach.sanitizer import Cleaner

url='https://amp.cnn.com/cnn/business/live-news/stock-market-news-101420/index.html'
x = requests.get(url)
soup = BeautifulSoup(x.content, 'html.parser') 

#soup = BeautifulSoup(x.content, 'html.parser')   
allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike', 'strong',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul', 'video', 'audio']

html_cleaner = Cleaner(
    scripts=True,
    javascript=True,
    comments=True,
    style=True,
    links=True,
    meta=False,
    add_nofollow=False,
    page_structure=False,
    processing_instructions=True,
    embedded=False,
    frames=False,
    forms=False,
    annoying_tags=False,
    remove_tags=None,
    remove_unknown_tags=False,
    safe_attrs_only=False
)
doc = html_cleaner.clean(str(soup), strip_comments=False)
print(doc)
#styles = ['color', 'font-weight']
#bleaching=bleach.clean(soup.prettify(),tags=allowed_tags,strip=True)
#tree = BeautifulSoup(x.content, "lxml")

#print(soup)
