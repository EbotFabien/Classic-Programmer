import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
from google.colab import files
#Libraries are imported

original_url = input("Enter the website url: ") 

unscraped = deque([original_url]) #The sites are added to a deque,a data structure that enables the removal of data either from left or right 

scraped = set() #This will contain the sites already scraped  

emails = set()  #When the Emails are scraped,the are stored here

while len(unscraped):# This while statement ends when all the  sites have been scraped 
    url = unscraped.popleft()  #get the url
    scraped.add(url)#Stored as scraped at once

    parts = urlsplit(url)
        
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    if '/' in parts.path: #Permits to get the url proper without any pages open 
      path = url[:url.rfind('/')+1]
    else:
      path = url

    print("Crawling URL %s" % url)
    try:
        response = requests.get(url) #opens the url to get info
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I))
    emails.update(new_emails) #All emails are gotten from their format structure using  Python regular regression

    soup = BeautifulSoup(response.text, 'lxml')
 #Decides to find all links in the site using beautiful soup 
    for anchor in soup.find_all("a"):
      if "href" in anchor.attrs:
        link = anchor.attrs["href"]
      else:
        link = ''

        if link.startswith('/'):
            link = base_url + link
        
        elif not link.startswith('http'):
            link = path + link

        if not link.endswith(".gz"):
          if not link in unscraped and not link in scraped:#if links are not found in both scraped and unscraped,add the link to unscraped
              unscraped.append(link)
#Emails sent to a csv file
df = pd.DataFrame(emails, columns=["Email"])
df.to_csv('email.csv', index=False)

files.download("email.csv")
