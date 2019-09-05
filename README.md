# Airtable-Scraper


                          Scraping a (specific) website containing an airtable to filter for student jobs.

The website: https://airtable.com/shrl5EIxGUExC3umi/tblvOwxPcPVcFmwxt
The Scraper: Python's "Beautiful Soup" v4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

IDEA:
The idea is to learn how to navigate a scraper through a webite. Still learning what that entails.

STEPS:
If I understand correctly how a websites and scrapers work these are the steps for executing this project's mission:
  1. Find the data part in the website, specifically the addresses of the companies.
  2. Visit each web address and look for these keywords: "Student", "Part-Time" and "Intern"
  
  
Comments:
  1.  I have finally understood that the "data-part" on the website is not there unless the user does some kind of an event. Now I am looking into what this event exactly is (mouse scroll/hover/click?) and how to simulate this event with Selenium's python "chromedriver".
