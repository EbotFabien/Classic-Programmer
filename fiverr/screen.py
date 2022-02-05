from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import ssl
from tqdm import tqdm

class InstaBot:
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        chromeOptions=webdriver.ChromeOptions()
        a=['https://www.callcentersindia.com/showall-orig.php?value1=411712_Pharmacy_Shipping__US-US__with_express_dlv_TAPENTADOL_BELBEIN_JPDOL_ADDERALL_KSALOL_perco__HYDRO', 'https://www.callcentersindia.com/showall-orig.php?value1=411711_VOIP_MINUTES_for_UK__USA_-_Free_Testing_Provided_For_Quality_Checking', 'https://www.callcentersindia.com/showall-orig.php?value1=411710_DID_NUMBER_for_UK__USA_with_Replacement_Guarantee', 'https://www.callcentersindia.com/showall-orig.php?value1=411709_VOIP_MINUTES_for_UK__USA_-_Free_Testing_Provided_For_Quality_Check']
        self.driver = webdriver.Chrome(executable_path='C:/python/bot/c/chromedriver.exe')
        
        num=[]
        for i in range(0,len(a)+1):
            num.append(i)
            
        for i in tqdm(a):
            nu=4
            name=(i[65:80])+str(nu)
            self.driver.get(i)
            sleep(5)
            element=self.driver.find_element_by_xpath('//*[@id="content_wrapper"]/div[2]/div[1]/table[2]/tbody/tr/td/table[2]')
            

            element.screenshot(name+'.png')
            



InstaBot()
