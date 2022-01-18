import requests
from bs4 import BeautifulSoup
import bleach
import markdown

url='https://amp.cnn.com/cnn/business/live-news/stock-market-news-101420/index.html'
x = requests.get(url)
soup = BeautifulSoup(x.content, 'html.parser') 
allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike', 'strong',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul', 'video', 'audio'] 


body_html = bleach.linkify(bleach.clean(soup.text,tags=allowed_tags, strip=True))
md = markdown.Markdown(output_format='html')
a= md.convert(body_html)
#a=markdown(body_html, output_format='html')
print(a)

allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike', 'strong',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul', 'video', 'audio']
