from bs4 import BeautifulSoup
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import sqlite3
import requests
import urllib.error
import urllib.parse
import urllib.robotparser 

url =urlopen('http://podcasts.joerogan.net/feed')#news feed site
xmldoc = parse(url)#parse Xml file
con = sqlite3.connect('mydatabase.db')


def sql_table(con):
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE pod_data(id integer PRIMARY KEY,title text, date text, linktopod text,podlink text)")
 
    con.commit()


def sql_insert(con,xmldoc):
    for item in xmldoc.iterfind('channel/item'):#iterate xml to find all the 'channel/item'
        realpod=item.findtext('link')#podcast link
        title=item.findtext('title')
        data = requests.get(str(realpod))#this is where we start using beautifulsoup to scrape the real podcast link
        soup = BeautifulSoup(data.content, 'html.parser')
        container =soup.find("div", {"class": "ajax-container"})#Big div contains all the other div's ,we section  the divs to penetrate better
        links = container.find(class_='podcast-links')
        anchor = links.find(class_='related-links-list')
        attach=anchor.find_all("a")
        final=attach[2]
        for data in final:
                source = final['href']#final podcast link
        entities=(item.findtext('title'), item.findtext('pubDate'),item.findtext('link'),source)
        cursorObj = con.cursor()
        cursorObj.execute("select * from pod_data where title= ?", (title,))
        data = cursorObj.fetchone()
        if data is None:
            cursorObj.execute('INSERT INTO pod_data(title, date, linktopod,podlink) VALUES(?, ?, ?,?)', entities)
        else:
            print(item.findtext('title'),"already exists")
       

    con.commit()


sql_insert(con,xmldoc)
#sql_table(con)

    
