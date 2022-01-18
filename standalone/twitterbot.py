from urllib.request import urlopen
from xml.etree.ElementTree import parse
import sqlite3

url =urlopen('https://twitrss.me/twitter_user_to_rss/?user=etuboleslie')
xmldoc = parse(url)
con = sqlite3.connect('mydatabase.db')


def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE twitterbot(id integer PRIMARY KEY,title text, date text, description text)")
 
    con.commit()

def sql_insert(con,xmldoc):
    for item in xmldoc.iterfind('channel/item'):
         entities=(item.findtext('title'), item.findtext('pubDate'),item.findtext('description'))    
         title=item.findtext('title')
         cursorObj = con.cursor()
         cursorObj.execute("select * from twitterbot where title= ?", (title,))
         data = cursorObj.fetchone()
         if data is None:
             cursorObj.execute('INSERT INTO twitterbot(title, date, description) VALUES(?, ?, ?)', entities)
         else:
            print(item.findtext('title'),"already exists")
       

    con.commit()

         
sql_table(con) 
sql_insert(con, xmldoc)
