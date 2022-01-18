import urllib.request
import json
from urllib.request import urlopen
import sqlite3 

url=["https://newsapi.org/v2/everything?sources=abc-news&apiKey=4cfd2c040b7b45eb82dbef82fe3b67a7","https://newsapi.org/v2/everything?sources=abc-news-au&apiKey=4cfd2c040b7b45eb82dbef82fe3b67a7"]
for i  in url:
    with urlopen(i) as url:
            response = url.read()

            
data = json.loads(response) #loads the Json data
con = sqlite3.connect('mydatabase.db')

def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE ABC_data(id integer PRIMARY KEY,id_json interger, author text, title text,description text, date text,content text)")
 
    con.commit()
 
def sql_insert(con,data):
    for i in data['articles']:#loop in the Json data to get the following titles
        entities=(i['source']['id'],i['author'],i['title'],i['description'],i['publishedAt'],i['content'])
        date = i['publishedAt']
        author = i['author']  
        cursorObj = con.cursor()
        cursorObj.execute("select rowid from ABC_data where date =? AND author = ? ", (date,author))
        data = cursorObj.fetchone()
        if data is None:
             cursorObj.execute('INSERT INTO ABC_data(id_json, author, title, description, date,content) VALUES(?, ?, ?, ?, ?,?)', entities)
        else:
            print(i['author'],"already exists")
             
       
           
       
          

                      
    con.commit()
 


    
sql_insert(con,data)

#sql_table(con)
