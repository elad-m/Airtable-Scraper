# these are just for getting opening a site in chrome through selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# these are for explicit waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.touch_actions import TouchActions

import sys


options = Options()  # this is here because it didn't work the easy way
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser  = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\Elad\AppData\Local\chromedriver\chromedriver.exe", )

browser.get("https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide")

try:
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located
    ((By.CLASS_NAME, "antiscroll-scrollbar")))
    browser.maximize_window()
    list_of_obj = browser.find_elements_by_class_name("url")
    print(len(list_of_obj))
    
    scrollbar_style = browser.find_element_by_class_name(
    "antiscroll-scrollbar-vertical").get_attribute("style")
    print(scrollbar_style)
    
    
    list_of_obj = browser.find_elements_by_class_name("url")
    print(len(list_of_obj))
    
    
    ## i think scrolling need to use touch and that might not be allowed
    ## in this site?
    
    
    

    
except Exception:
    print("there was an exception:", 
    sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
 
browser.quit()


# print(some_str + "transform: translated3d(0px, , 0px);")

  # js = "return document.getElementsByClassName('paneInnerContent')[3].getAttribute('style');"
    
    # some_str = browser.execute_script(js) 
    # for i in range(len(list_of_obj)):
        # print(list_of_obj[i].text)