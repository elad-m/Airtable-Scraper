# importing an httplib2 and Beautiful Soup packages
import httplib2
from bs4 import BeautifulSoup

# The that is the main goal
airtable_url = "https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide"

# Simpler website to practice
ezurl = "https://www.dragonflycave.com/mechanics/stat-stages"


def find_parents(tag):
    counter = 0
    cur_parent = tag.parent
    if cur_parent is not None and "id" in cur_parent:
        print(cur_parent["id"])
        print("counter", counter)
    while cur_parent is not None:
        counter += 1
        cur_parent = cur_parent.parent
        if cur_parent is not None and "id" in cur_parent:
            print(cur_parent["id"])
        print("counter", counter)
  
# import re

def traverse_tree_to_target_tag(tar_tag, cls, soup):
    what = soup.find_all("div", {"class": "paneInnerContent"})
    print(len(what))
    # cur_child = soup
    # print(cur_child.name)
    
    # cur_child = soup.child


airtable_file  = open("airtable.html")
soup = BeautifulSoup(airtable_file, "html.parser")
if soup.find("div", {"class": "paneInnerContent"}):
    traverse_tree_to_target_tag("div", "paneInnerContent", soup)



## an attempt to read line by line until the tag
# if "paneInnerContent" in airtable_file.read():
    # airtable_file.seek(0)
    # line = airtable_file.readline()
    # print("line: ", line)
# else:
    # pass



  
## an attempt to print the target tag's parents names/ids    
# http = httplib2.Http()
# status, response = http.request(airtable_url)
# airtable_file  = open("airtable.html")
# bs = BeautifulSoup(airtable_file, "html.parser")
# some_tag = bs.find("div", {"class": "paneInnerContent"})
# print("THE TAG:          \n", some_tag)
# print(find_parents(some_tag))



# This is what I used to print the WHOLE tag with id=content on the ezurl
# it does not work for some reason for the airtable
# possible solutions are: look for scraping airtable website, or printing the 
# parents of the paneInnerContent tag
# print((bs.find("div", {"id": "content"})))




####################################################################################
#                           Various Tryout Code Snippets                           #
####################################################################################


# The following is a cemetary for failed attempts. Please be respective


# for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
    # if link.has_attr('href'):
        # print(link['href'])

        
# query the website and return the html to the variable ‘page’

# req = Request(airtable_url)
# try:
    # response = urlopen(req)
# except HTTPError as e:
    # print('The server couldn\'t fulfill the request.')
    # print('Error code: ', e.code)
# except URLError as e:
    # print('We failed to reach a server.')
    # print('Reason: ', e.reason)
# else:

    # parse the html using beautiful soup and store in variable `soup`
    # page = str(response.read())
    # soup = BeautifulSoup(page, "html.parser")

    
    # for a in soup.find_all('a', href=True):
        # print("Found the URL:" + a['href'])
    
    # print(soup("span"))
    # print(soup.find_all("span.url"))
    # res = soup.find_all("div", class_="url")
    # print(res)
    # for r in res:
        # print(type(r))
        

        
# import requests
# r = requests.get(airtable_url)
# html_content = r.text
# soup = BeautifulSoup(html_content, 'lxml')
# print(soup.find_all('a'))
