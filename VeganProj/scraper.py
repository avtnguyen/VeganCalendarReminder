import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup

URL = "https://www.xemlicham.com/am-lich/nam/"

for yr in range(2017, 2031):
    
    URL_yr = urljoin(URL, str(yr))
   
    r = requests.get(URL_yr)

    filePath = 'data/raw/' + str(yr) +'.txt'

    if not os.path.exists(filePath):    
        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(r.text)
        print(f"Webscraping sucess for {yr}! file is stored in {filePath}")
    else: 
        print('Raw file is already exist')
    
