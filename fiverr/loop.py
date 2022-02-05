import requests
from bs4 import BeautifulSoup
import ssl

url='https://www.callcentersindia.com/call_center_forum.php'
ssl._create_default_https_context = ssl._create_unverified_context
x = requests.get(url)
link=[]
soup = BeautifulSoup(x.content, 'html.parser')
main=soup.find( class_ = "main_content" )
div_sec=main.findAll('div')[0]
table=div_sec.findAll('table')[0]
main_table=table.findAll('table')[0]
titles=main_table.findAll('tr')#loop here from here to the last
for i in titles:
    try:
        links=i.findAll('a')[0]
        link.append('https://www.callcentersindia.com/'+links.get('href'))
    except:
        print('No link')

print(link)

