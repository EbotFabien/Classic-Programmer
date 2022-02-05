import requests
from bs4 import BeautifulSoup
import ssl
from time import sleep
from tqdm import tqdm

url='https://www.callcentersindia.com/call_center_forum.php'
ssl._create_default_https_context = ssl._create_unverified_context
x = requests.get(url)
pagination_link=[]
link=[]
soup = BeautifulSoup(x.content, 'html.parser')
main=soup.find( class_ = "main_content" )
div_sec=main.findAll('div')[0]
#links to crop
table=div_sec.findAll('table')[0]
main_table=table.findAll('table')[0]
titles=main_table.findAll('tr')#loop here from here to the last
for i in titles:
    try:
        links=i.findAll('a')[0]
        link.append('https://www.callcentersindia.com/'+links.get('href'))
    except:
        print("Sorry, no link over here")
print("First link")
print(link)
print(len(link))
#pagination
pag=div_sec.find_all_next("table")[-1]
pag_links=main.find(class_ ='pagenumlink')#first
last_link=pag_links.find_all_next(class_ ='pagenumlink')[-1]
linka='https://www.callcentersindia.com/'+pag_links.get('href')[0:-1]
start=int(pag_links.string)
end=int(last_link.string)

for num in range(start,end+1):
    pagination_link.append(linka+str(num))

#links from all pagination
for linked in tqdm(pagination_link):
    #sleep(2)
    url=linked
    ssl._create_default_https_context = ssl._create_unverified_context
    x = requests.get(url)
    pagination_link=[]
    soup = BeautifulSoup(x.content, 'html.parser')
    main=soup.find( class_ = "main_content" )
    div_sec=main.findAll('div')[0]
    #links to crop
    table=div_sec.findAll('table')[0]
    main_table=table.findAll('table')[0]
    titles=main_table.findAll('tr')#loop here from here to the last
    for i in titles:
        try:
            links=i.findAll('a')[0]
            link.append('https://www.callcentersindia.com/'+links.get('href'))
        except:
            a='No link'

print('last')
print(link)
print(len(link))
