# these are just for getting opening a site in chrome through selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# these are for explicit waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
import sys


options = Options()  # this is here because it didn't work the easy way
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver  = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\Elad\AppData\Local\chromedriver\chromedriver.exe", )

driver.get("https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide")

try:
    
    driver.maximize_window()
    for px_to_scroll in range(0, 383, 9):
        # wait for scrollbar and scroll by px_to_scroll
        WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                       ((By.CLASS_NAME, "antiscroll-scrollbar-vertical")))
        # scrollbar = driver.find_element_by_class_name("antiscroll-scrollbar-vertical")
        ActionChains(driver).move_to_element(driver.find_element_by_class_name("antiscroll-scrollbar-vertical")
               ).drag_and_drop_by_offset(driver.find_element_by_class_name(
               "antiscroll-scrollbar-vertical"), 0, px_to_scroll).perform()
    
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located
        ((By.CLASS_NAME, "numberText")))
        list_of_obj = driver.find_elements_by_class_name("numberText")
        row_num_string = ""
        for i in range(len(list_of_obj)):
            row_num_string += list_of_obj[i].text + ", "
        print(row_num_string, "END")
        # print("len: ", len(list_of_obj))
       
        driver.refresh()
    
    ## TODO: handle the moveTargetOutOfBound exception
    ## write to a new file that deletes the previous
    ## write the urls  and not the numbers
    

    
except Exception:
    print("there was an exception:", 
          sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2], 
          "LINE: ", sys.exc_info()[2].tb_lineno)
    
 
driver.quit()


# print(some_str + "transform: translated3d(0px, , 0px);")

  # js = "return document.getElementsByClassName('paneInnerContent')[3].getAttribute('style');"
    
    # some_str = driver.execute_script(js) 
    # for i in range(len(list_of_obj)):
        # print(list_of_obj[i].text)