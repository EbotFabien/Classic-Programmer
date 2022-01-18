from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import sqlite3
import requests

url =urlopen('http://podcasts.joerogan.net/feed')
xmldoc = parse(url)
con = sqlite3.connect('mydatabase.db')


def sql_table(con):
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE pod_data(id integer PRIMARY KEY,title text, date text, linktopod text,podlink text)")
 
    con.commit()
 
def sql_insert(con,xmldoc):
    for item in xmldoc.iterfind('channel/item'):
        realpod=item.findtext('link')
        title=item.findtext('title')
        driver = webdriver.PhantomJS(executable_path='C:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        driver.implicitly_wait(10)
        driver.get(str(realpod))
        element = driver.find_element_by_css_selector('button.play-podcast')
        url=element.get_attribute('outerHTML')
        soup = BeautifulSoup(url,"lxml")
        timeline = soup.select('button.play-podcast')
        for data in timeline:
            source = data['data-stream-url']
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


