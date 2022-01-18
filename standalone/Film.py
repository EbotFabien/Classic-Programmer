from bs4 import BeautifulSoup
import requests

def bot():
    u="http://dl.mellimovies.com/Movie_EN/98/"
    i=1
    for i in range(5):
        print(u+i+"/")
    #url=requests.get(u).text
    #soup = BeautifulSoup(url,'lxml')
    #print(soup.prettify())
    



bot()
