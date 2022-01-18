import requests
import urllib.error
import urllib.parse
import urllib.robotparser 
from urllib.request import build_opener
from bs4 import BeautifulSoup
from urllib.request import urlopen


def Real(a):
    url=(a)
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    timeline =soup.find("div", {"class": "ajax-container"})
    ford = timeline.find(class_='podcast-links')
    anchor = ford.find(class_='related-links-list')
    attach=anchor.find_all("a")
    final=attach[2]
    for data in final:
            source = final['href']
   
    print(source)


Real('http://podcasts.joerogan.net/podcasts/sean-carroll-3')

     

##import urllib.error
#import urllib.parse
#import urllib.robotparser 
#from urllib.request import build_opener
#from bs4 import BeautifulSoup
##from urllib.request import urlopen


#def Real(a):
 ##  data = requests.get(url)
   # soup = BeautifulSoup(data.content, 'html.parser')
    #soup.find_element_b
    #print(soup)



#Real('https://www.instagram.com/')
