from urllib.request import urlopen
from xml.etree.ElementTree import parse
import sqlite3

url =urlopen('http://feeds.bbci.co.uk/news/rss.xml')
xmldoc = parse(url)
con = sqlite3.connect('mydatabase.db')


def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE BBC_data(id integer PRIMARY KEY,title text,description text, link text,date  text)")
 
    con.commit()

def sql_insert(con,xmldoc):
    for item in xmldoc.iterfind('channel/item'):
         entities=(item.findtext('title'),item.findtext('description'),item.findtext('link'),item.findtext('pubDate'))    
         title=item.findtext('title')
         cursorObj = con.cursor()
         cursorObj.execute("select * from BBC_data where title= ?", (title,))
         data = cursorObj.fetchone()
         if data is None:
             cursorObj.execute('INSERT INTO BBC_data(title,description,link,date) VALUES(?,?, ?, ?)', entities)
         else:
            print(item.findtext('title'),"already exists")
       

    con.commit()

         
#sql_table(con) 
sql_insert(con, xmldoc)
