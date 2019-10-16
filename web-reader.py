# these are just for getting opening a site in chrome through selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# these are for explicit waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys

from selenium.webdriver.common.action_chains import ActionChains
import sys
import csv

class RowsDict:
    """
    A dictionary of row numbers to pairs of row numbers and urls
    """

    def __init__(self):
        self._row_dict = {}
        self._size = 0

    def get_dict(self):
        return self._row_dict

    def get_size(self):
        return self._size

    def add(self, pair_to_add):
        assert type(pair_to_add) == tuple and len(pair_to_add) == 2
        row_num_to_add = pair_to_add[0]
        curr_size = self.get_size()
        if row_num_to_add != 1:
            assert self._row_dict[curr_size][0] == row_num_to_add - 1, "not the next line"  ## to say: this is not the next line number

        self._row_dict[row_num_to_add] = pair_to_add
        self._size = len(self.get_dict())

    def print_dict(self, end=None, start=1):
        """
        Print all values of dict by the order of the keys, from start to end param
        :param end:
        :param start:
        :return:
        """
        print_str = ""
        if end is None:
            end = self._size + 1
        for i in range(start, end, 1):
            print_str += str(self._row_dict[i])
        print(print_str)
        

def unit_test_row_dict():
    # test init - attribute
    a = RowsDict()
    print(a.get_dict(), a.get_size())

    # test add
    p = (1, "asdf")
    a.add(p)
    print(a.get_dict(), a.get_size())
    a.print_dict()
    # test add a line that is  next
    p2 = (2, "aasdfaqwesdf")
    a.add(p2)
    print(a.get_dict(), a.get_size())
    a.print_dict()
    # test add a line that is NOT next
    # p5 = (5, "hey")
    # a.add(p5)
    list_of_pairs = list(zip([i for i in range(3, 13)], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]))
    for j in range(0, 10):
        a.add(list_of_pairs[j])
    a.print_dict()
    print(a.get_dict()[11])



def get_chrome_web_driver(binary_location, executable_path_str, web_url):
    options = Options()  # this is here because it didn't work the easy way
    options.binary_location = binary_location
    options.add_argument("--disable-infobars --disable-extensions")
    driver  = webdriver.Chrome(chrome_options=options, executable_path=executable_path_str, )
    driver.get(web_url)
    return driver


def get_num_of_records(driver):
    WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located
                                           ((By.CLASS_NAME, "summaryCell")))
    summary_cell_webelement = driver.find_element_by_class_name("summaryCell")
    return int(summary_cell_webelement.text.split()[0])


def move_down_one_row(driver, row_webelement, row_num):
    if row_num == 1:
        actions = ActionChains(driver)
        actions.move_to_element(row_webelement).click()
        actions.send_keys(keys.Keys.ARROW_DOWN).perform()
    else:
        actions = ActionChains(driver)
        actions.send_keys(keys.Keys.ARROW_DOWN).perform()

def get_row_url(driver, row_num, rows_dict_object):
    if row_num == 1:
        search_keyword = 'firstRow'
    else:
        search_keyword = 'cursorCell'
    try:
        condition = EC.presence_of_element_located((By.CLASS_NAME, search_keyword))
        WebDriverWait(driver, 7, 0.1).until(condition)
        row_webelement = driver.find_element_by_class_name(search_keyword)
        assert row_webelement is not None, "Could not get the row"
        
        row_id = row_webelement.get_attribute("data-rowid")
        css_selector_str = ".dataRow.rightPane[data-rowid='" + row_id + "']"
        entire_right_pane_row = driver.find_element_by_css_selector(css_selector_str)
        row_url = entire_right_pane_row.find_element_by_css_selector(".url")
        assert row_url is not None, "Could not get URL of row"
        # print("Row pair: ", "(" + str(row_num)+ ", " + row_url.text + ")")
        rows_dict_object.add((row_num, row_url.text))
        
        move_down_one_row(driver, row_webelement, row_num)
        
    except Exception:
        print("There was an exception:", 
              sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2], 
              "LINE: ", sys.exc_info()[2].tb_lineno)
        raise
    
    
def main():
    
    driver = get_chrome_web_driver("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                                    r"C:\Users\Elad\AppData\Local\chromedriver\chromedriver.exe",
                                    "https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide")
    try:
        driver.maximize_window()
        num_of_records = get_num_of_records(driver) ## change later
        rows_dict_object = RowsDict()
               
        for row_num in range(1, num_of_records + 1):
            get_row_url(driver, row_num, rows_dict_object)
            if row_num % 10 == 0:
                # rows_dict_object.print_dict(row_num + 1, row_num  - 9)
                pass
        f = open("output.csv", "w+", newline='')
        w = csv.writer(f)
        for key, val in rows_dict_object.get_dict().items():
            w.writerow([key, val])
        f.close()
        
    except Exception:
        print("there was an exception:", 
              sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2], 
              "LINE: ", sys.exc_info()[2].tb_lineno)
    
    driver.quit()
    


if __name__== "__main__":
    # unit_test_row_dict()
    main()

 
