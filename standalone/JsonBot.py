import urllib.request
import json
from urllib.request import urlopen
import sqlite3 

url="https://api.github.com/users"
with urlopen(url) as url:
        response = url.read()
data = json.loads(response) 
con = sqlite3.connect('mydatabase.db')

def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE Jsonn_data(id integer PRIMARY KEY,id_json interger, login text, node_id text, type text,site_admin boolean)")
 
    con.commit()
 
def sql_insert(con,data):
    for i in data:
        entities=(i['id'],i['login'],i['node_id'],i['type'],i['site_admin'])
        ide = i['id']
        cursorObj = con.cursor()
        cursorObj.execute("select rowid from Jsonn_data where id_json = ?", (ide,))
        data = cursorObj.fetchone()
        if data is None:
             cursorObj.execute('INSERT INTO Jsonn_data(id_json, login, node_id, type, site_admin) VALUES(?, ?, ?, ?, ?)', entities)
        else:
            print(i['login'],"already exists")
             
       
           
       
          

                      
    con.commit()
 


    
sql_insert(con,data)

#sql_table(con)
