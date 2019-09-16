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


def get_num_of_records(driver):
    WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located
                                           ((By.CLASS_NAME, "summaryCell")))
    summary_cell_webelement = driver.find_element_by_class_name("summaryCell")
    return summary_cell_webelement.text.split()[0]
     
    
    
try:
    
    driver.maximize_window()
    num_of_records = get_num_of_records(driver)  # this would be a string
    print("number of records: ", num_of_records)
    px_to_scroll = 8
    row_num_string = ""
    rows_dic = {}
    for i in range(int(num_of_records)):
        if i != 0:  # not scrolling the first time
            # wait for scrollbar and scroll by px_to_scroll
            WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located
                                           ((By.CLASS_NAME, "antiscroll-scrollbar-vertical")))
            
            actions = ActionChains(driver)
            scrollbar = driver.find_element_by_class_name("antiscroll-scrollbar-vertical")
            actions.move_to_element(scrollbar)
            actions.drag_and_drop_by_offset(scrollbar, 0, px_to_scroll).perform()
    
        WebDriverWait(driver, 10, 1).until(EC.presence_of_all_elements_located
        ((By.CLASS_NAME, "numberText"))) # that is the class name of the element of row number 
        ##todo this wait should be a variable: wait to get the next dataRow
        pane_inner_content = driver.find_element_by_class_name("paneInnerContent")
        ## here you need dataLeftPane and right. You have multiple paneInnerContent-s
        ## because url and row number are on different divs
        list_of_obj = pane_inner_content.find_elements_by_css_selector("div.dataRow.leftPane")
        # list_of_obj = driver.find_elements_by_class_name("numberText")
        temp_str = ""
        for i in range(len(list_of_obj)):
            curr_elem = list_of_obj[i]
            if curr_elem.is_displayed():
                temp_str += curr_elem.text + ", "
                row_num_string += temp_str
        # print(temp_str)
        driver.refresh()
        print(row_num_string[-5:])
    
    print(row_num_string, "END")
    ## problems:
    ## not stopping ...
    ## -still scrolling too much - a lot of jobs missing.
    ## -stale element happens on a whim apparently, maybe internet connection? non-deterministic
    ## change the condition of the for loop for what it really is
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