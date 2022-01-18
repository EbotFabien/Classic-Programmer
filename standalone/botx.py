from urllib.request import urlopen
from xml.etree.ElementTree import parse
import sqlite3

url =urlopen('https://blogs.oracle.com/oraclepartners/database-7/rss')
xmldoc = parse(url)
con = sqlite3.connect('mydatabase.db')


def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE xml_data(id integer PRIMARY KEY,title text, date text, link text)")
 
    con.commit()

def sql_insert(con,xmldoc):
    for item in xmldoc.iterfind('channel/item'):
         entities=(item.findtext('title'), item.findtext('pubDate'),item.findtext('link'))    
         title=item.findtext('title')
         cursorObj = con.cursor()
         cursorObj.execute("select * from xml_data where title= ?", (title,))
         data = cursorObj.fetchone()
         if data is None:
             cursorObj.execute('INSERT INTO xml_data(title, date, link) VALUES(?, ?, ?)', entities)
         else:
            print(item.findtext('title'),"already exists")
       

    con.commit()

         
#sql_table(con) 
sql_insert(con, xmldoc)
