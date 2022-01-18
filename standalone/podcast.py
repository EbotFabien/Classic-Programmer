from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver = webdriver.Edge()
#driver = webdriver.PhantomJS(executable_path='C:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("http://podcasts.joerogan.net/podcasts/sean-carroll-3")
element = driver.find_element_by_class_name('play-podcast')

url=element.get_attribute('outerHTML')
soup = BeautifulSoup(url,"lxml")
timeline = soup.select('button.play-podcast')
for data in timeline:
    source = data['data-stream-url']
    print(source)
#print (element.text)
#print (element.tag_name)
#print (element.parent)
#print (element.location)
#print (element.size)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaBot:
    def __init__(self,user_name,pwd):
        chromeOptions=webdriver.ChromeOptions()
        prefs ={'profile.managed_default_content_settings.images':2}
        chromeOptions.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(user_name)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        
        


InstaBot("fabien_classic","nexttel")

