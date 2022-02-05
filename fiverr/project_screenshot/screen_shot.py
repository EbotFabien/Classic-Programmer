import requests
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
from time import sleep
from tqdm import tqdm




class InstaBot:
    def __init__(self,url,link):
        x = requests.get(url)
        self.link=link
        self.pagination_link=[]
        soup = BeautifulSoup(x.content, 'html.parser')
        self.main=soup.find( class_ = "main_content" )
        self.div_sec=self.main.findAll('div')[0]
        self.count=0
        #links to crop
        table=self.div_sec.findAll('table')[0]
        main_table=table.findAll('table')[0]
        titles=main_table.findAll('tr')#loop here from here to the last
        for i in titles:
            try:
                links=i.findAll('a')[0]
                self.link.append('https://www.callcentersindia.com/'+links.get('href'))
            except:
                a='No link'

    def get_pagination(self):
        #pagination
        pag=self.div_sec.find_all_next("table")[-1]
        pag_links=self.main.find(class_ ='pagenumlink')#first
        last_link=pag_links.find_all_next(class_ ='pagenumlink')[-1]
        linka='https://www.callcentersindia.com/'+pag_links.get('href')[0:-1]
        start=int(pag_links.string)
        end=int(last_link.string)

        for num in range(start,end+1):
            self.pagination_link.append(linka+str(num))

    def final_link(self):
        #final_links
        for linked in tqdm(self.pagination_link):
            InstaBot(linked,self.link)

    def picture(self):
        #screenshots
        chromeOptions=webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        #num=[]
        #for i in range(0,len(self.link)+1):
            #num.append(i)
            
        for i in tqdm(self.link):#zip(self.link,num):
            name=('screen')+str(self.count)
            driver.get(i)
            sleep(5)
            element=driver.find_element_by_xpath('//*[@id="content_wrapper"]/div[2]/div[1]/table[2]')

            element.screenshot(name+'.png')
            self.count=self.count+1


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    
    My_bot=InstaBot("https://www.callcentersindia.com/call_center_forum.php",[])
    My_bot.get_pagination()
    My_bot.final_link()
    My_bot.picture()

            
