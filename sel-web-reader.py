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

import time


options = Options()  # this is here because it didn't work the easy way
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver  = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\Elad\AppData\Local\chromedriver\chromedriver.exe", )

driver.get("https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide")

try:
    
    driver.maximize_window()
    px_to_scroll = 8
    for i in range(42):  # 42 scrolling for 9px scroll for a 383px scroll bar
        if i != 0:  # not scrolling the first time
            # wait for scrollbar and scroll by px_to_scroll
            WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located
                                           ((By.CLASS_NAME, "antiscroll-scrollbar-vertical")))
            
            # start_time = time.time()
            # WebDriverWait(driver, 50, 0.3).until(EC.staleness_of(scrollbar))
            # end_time = time.time()
            # print("time: ", end_time - start_time)
            actions = ActionChains(driver)
            scrollbar = driver.find_element_by_class_name("antiscroll-scrollbar-vertical")
            actions.move_to_element(driver.find_element_by_class_name("antiscroll-scrollbar-vertical"))
            actions.drag_and_drop_by_offset(driver.find_element_by_class_name(
                   "antiscroll-scrollbar-vertical"), 0, px_to_scroll).perform()
    
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located
        ((By.CLASS_NAME, "numberText")))
        list_of_obj = driver.find_elements_by_class_name("numberText")
        row_num_string = ""
        for i in range(len(list_of_obj)):
            curr_elem = list_of_obj[i]
            if curr_elem.is_displayed():
                row_num_string += curr_elem.text + ", "
        print(row_num_string, "END")
        # print("len: ", len(list_of_obj))
       
        driver.refresh()
    
    ## problems:
    ## -stale element happens on a whim apparently, maybe internet connection? non-deterministic
    ## -still scrolling too much - a lot of jobs missing.
    ## -not able to scroll the page for trials using js console: 
    
    # document.getElementsByClassName('antiscroll-scrollbar-vertical')[0].style.transform = "translate3d(0, 9, 0)";
# "translate3d(0, 9, 0)"
    
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