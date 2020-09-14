# This project scraps myCareer Website for new Jobs and notifies my friends through What's App.
# Creator: Ahmad Kammonah - Date: Sep, 2020 - Copyright: Kammonah Industries 2020

import csv  # Package used to easily convert list into csv format (Excel Sheet format)
import requests  # Package used to request a website
import datetime  # Package used to get time and date. Used for logging purposes
from bs4 import BeautifulSoup  # Package used to easily handle html (language used to write websites)
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# TODO: ADD Headers which can be found in network tab in inspect element
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

# TODO: ADD Login Data here. Can be found in Network tab in inspect element
login_data = {
    '__RequestVerificationToken': 'MZ-cDsRgR4aj3_7ABTC8wD_u2KJ5ji8Oy5Spx1yFShAw1n5tMchuaYRV16RwGOMkSd_nAMy0UUsM9T9jzkj5PYGvt_BKmSmKwe-6SBE-Iwo1',
    'UserName': '****',
    'Password': '****',
    'returnUrl': '/Program/GetProducts?classification=f22e8568-5cb8-464f-93f6-b390759240de'
}
'''
cookies = {
    '__RequestVerificationToken': 'MZ-cDsRgR4aj3_7ABTC8wD_u2KJ5ji8Oy5Spx1yFShAw1n5tMchuaYRV16RwGOMkSd_nAMy0UUsM9T9jzkj5PYGvt_BKmSmKwe-6SBE-Iwo1
}
'''
# TODO: Add login urls and other required pages' urls here
login_url = "https://www.dalsports.dal.ca/Program/GetProducts?classification=f22e8568-5cb8-464f-93f6-b390759240de"

# Opens a request session and goes to requested page (JOB POSTING PAGE)
with requests.Session() as s:
    a7a = s.post(login_url, data=login_data)  # requests to go to desired website
    soup = BeautifulSoup(a7a.content, 'lxml')  # passes the content of the page to Beautiful Soup Package

print(soup)
