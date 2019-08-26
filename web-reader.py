# importing an httplib2 and Beautiful Soup packages
import httplib2
from bs4 import BeautifulSoup

# The that is the main goal
airtable_url = "https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt?blocks=hide"

# Simpler website to practice
ezurl = "https://www.dragonflycave.com/mechanics/stat-stages"



http = httplib2.Http()
status, response = http.request(ezurl)
bs = BeautifulSoup(response, "html.parser")

def find_descendant_with_id(bs_obj, id_str):
    for child in bs_obj.html.descendants:
        print(child.name)
        
    print("THE END")

# find_descendant_with_id(bs, "layout")


print((bs.find("div", {"id": "content"})))

# testing comment


####################################################################################
#                           Various Tryout Code Snippets                           #
####################################################################################

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
