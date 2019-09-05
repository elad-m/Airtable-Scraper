# these are just for getting opening a site in chrome through selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# these are for explicit waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys


options = Options()  # this is here because it didn't work the easy way
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser  = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\Elad\AppData\Local\chromedriver\chromedriver.exe", )

browser.get("https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide")

try:

    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located
    ((By.CLASS_NAME, "url")))
    list_of_obj = browser.find_elements_by_class_name("url")
    print(list_of_obj[0].text)
    
    
    
    
    

    
except Exception:
    print("there was an exception:", sys.exc_info()[0], sys.exc_info()[1],
    sys.exc_info()[2])
    
 
browser.quit()


    
#example 1
# from selenium.webdriver.common.keys import Keys

# assert 'Yahoo' in browser.title

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
