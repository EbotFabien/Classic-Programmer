import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser 
from urllib.request import build_opener
from bs4 import BeautifulSoup
import requests
import re
import time

def Real(a):
    opener = build_opener()
    #add=request.add_header[('User-agent','Mozilla/5.0')]
    opener.addheaders =[('User-agent','Mozilla/5.0')]
    url=(a)
    ourUrl = opener.open(url).read()
    # Make a GET request to fetch the raw HTML content
    #html_content = requests.get(url).text
    # Parse the html content
    soup = BeautifulSoup(ourUrl,"lxml")
    for link in soup.findAll('a',attrs={'href':re.compile("^/wiki/")}):
         find = re.compile('/wiki/(.*?)"')
         searchMovie = re.search(find,str(link))
         movie = searchMovie.group(1)
         opener = build_opener()
         opener.addheaders =[('User-agent','Mozilla/5.0')]
         url=('https://en.wikipedia.org/wiki/' + movie)
         ourUrl = opener.open(url).read()
         soup = BeautifulSoup(ourUrl,"lxml")
         print (soup.title.text)
         time.sleep(2)
    return 1





Real('https://en.wikipedia.org/wiki/List_of_United_States_comedy_films')

     
