import os
from bs4 import BeautifulSoup
import html5lib
import re
import json

for yr in range(2017, 2031):

    # Read the raw data file
    file_path_import = 'data/raw/'+ str(yr)+'.txt'
    with open(file_path_import, 'r', encoding='utf-8') as file:
        web_content = file.read()

    # Parse raw data into processed data with day, month, luna day, luna month

    soup = BeautifulSoup(web_content, 'html5lib') 

    data = []

    month_cal = soup.findAll('div',attrs = {'class':'col-md-12'})[1:13]

    for monthIdx in range(0, len(month_cal)):
        for day_in_month in range(1, len(month_cal[monthIdx].select('a'))):
            href = month_cal[monthIdx].select('a')[day_in_month].get('href')
            match = re.search(r'/thang/(\d+)', href)
            if match :
                month = match.group(1)
            day = month_cal[monthIdx].select('a')[day_in_month].find('div', attrs= {'class':'duong'}).text.split()[0]
            luna = month_cal[monthIdx].select('a')[day_in_month].find('div', attrs= {'class':'am'}).text
            if '/' in luna:
                luna_month = luna.split('/')[1].split(' ')[0]
                luna_day = luna.split('/')[0].strip()
            else:
                luna_day = luna.strip()

            #print(day, month, am_month, am_day)
            data_i = {'day' : day, 'month' : month, 'luna_day' : luna_day, 'luna_month' : luna_month}
            data.append(data_i)

    # Export processed data into the folder data/processed
    file_path_export = 'data/processed/' + 'processed_' + str(yr) +'.txt'

    with open(file_path_export,'w') as export_file:
        export_file.write(json.dumps(data))

    print('Finish process file {0}!'.format(yr))

