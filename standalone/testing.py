import itertools
from multiprocessing import Process
import sys
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
from xml.etree.ElementTree import parse
import sqlite3
import requests
import urllib.error
import urllib.parse
import urllib.robotparser 
import urllib.request
import json
from time import sleep




url='https://guardian.ng/category/news/nigeria/feed/'
news=[{'title': 'Edo Governorship Election: Oshiomhole Votes (Pictures)', 'link': 'http://www.nairaland.com/6129611/edo-governorship-election-oshiomhole-votes'}, {'title': 'Edo Election: Violence Erupts As Governor Obaseki Arrives His Polling Unit', 'link': 'http://www.nairaland.com/6129580/edo-election-violence-erupts-obaseki'}, {'title': 'Edo Election: APC Candidate, Ize-Iyamu Votes (Photos, Video)', 'link': 'http://www.nairaland.com/6129544/edo-governorship-election-ize-iyamu-votes'}, {'title': '2 Pastors Rape A Youth Corper During Prayers In Rivers State', 'link': 'http://www.nairaland.com/6129229/pastors-austin-emmanuel-peter-davies'}, {'title': "Wizkid 'No Stress' Is No1 In Nigeria & The US World Chart According To ITunes", 'link': 'http://www.nairaland.com/6129389/wizkid-no-stress-no1-nigeria'}, {'title': 'Edo Election: Voters Stop Thugs From Disrupting Election In Oredo (Video)', 'link': 'http://www.nairaland.com/6129444/edo-election-voters-stop-thugs'}, {'title': 'Ondo Election: Governor Akeredolu Shares Customized Ludo And Slippers', 'link': 'http://www.nairaland.com/6128491/governor-akeredolu-shares-ludo-slippers'}, {'title': 'Edo Election: Those Plotting To Buy Votes Today Won’t Succeed - INEC', 'link': 'http://www.nairaland.com/6129347/edo-governorship-election-those-plotting'}, {'title': 'Vigilante Stops Ondo Passengers From Entering Edo (Video)', 'link': 'http://www.nairaland.com/6129344/vigilante-stops-ondo-passengers-entering'}, {'title': "'40, Sexy, Successful & Happy - Linda Ikeji Celebrates Her 40th Birthday (Photos)", 'link': 'http://www.nairaland.com/6129293/linda-ikeji-celebrates-40th-birthday'}, {'title': 'Skepta Celebrates His 38th Birthday Today', 'link': 'http://www.nairaland.com/6129374/skepta-celebrates-38th-birthday-today'}, {'title': 'Amina Mama Celebrates Her 62nd Birthday Today', 'link': 'http://www.nairaland.com/6129359/amina-mama-celebrates-62nd-birthday'}]
response=requests.get(url)
soup=BeautifulSoup(response.text,features="xml")
print(soup.findAll('item'))
#for element in itertools.cycle(a)
#for i in news:
    #response=requests.get(i['link'])
    #soup=BeautifulSoup(response.content,'lxml')
    #metas=soup.findAll('meta')

    #for j in metas:
        #if j.get('property') == "og:image":
            #i['thumbnail']=j.get('content')
            




#print(news)





#property="og:image"