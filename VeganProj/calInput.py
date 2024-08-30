import os 
import json

# List of special holidays:
holiday = [{'holiday': 'tet nguyen dan', 'am day': 1, 'am month': 1}, {'holiday': 'tet nguyen dan', 'am day': 2, 'am month': 1}, 
           {'holiday': 'tet nguyen dan','am day': 3, 'am month' : 1}, {'holiday': 'tet nguyen dan', 'am day': 4, 'am month' : 1}, 
           {'holiday': 'tet nguyen tieu', 'am day': 15, 'am month' : 1}, {'holiday': 'tet han thuc', 'am day': 3, 'am month' : 3},
           {'holiday': 'gio to hung vuong', 'am day': 10, 'am month' : 3}, {'holiday': 'le phat dan', 'am day': 15, 'am month' : 4},
           {'holiday': 'tet doan ngo', 'am day': 5, 'am month' : 5}, {'holiday': 'le Vu Lan', 'am day': 15, 'am month' : 7},
           {'holiday': 'tet trung thu', 'am day': 15, 'am month' : 8}, {'holiday': 'le cung ong tao', 'am day': 23, 'am month' : 12}
        ]

# Read data json txt file:
data_file_path = 'data/processed/processed_' + '2020' + '.txt'
with open(data_file_path) as data_file:
    data = json.load(data_file)

# Function to check if the day is the 14th, 15th, the last day of each month and the first day of the next month
# in lunar calendar
# and if the day belong to the holiday list
def check_day(data, holiday):
    total_date = len(data)
    result = []
    holiday_date= []
    for i in range(total_date):
        # check last and first day for each am month:
        day_am = int(data[i]['am day'])
        month_am = int(data[i]['am month'])
        if day_am == 14 or day_am == 15:
           result.append(data[i])
        elif i != 0 and day_am == 1:
            result.append(data[i-1])
            result.append(data[i])
        elif i == 0 and day_am == 1:
            result.append(data[i])

        # check if date is in the holiday list:
        for j in range(len(holiday)):
            if day_am == holiday[j]['am day'] and month_am == holiday[j]['am month']: 
                holiday_date.append({'holiday': holiday[j]['holiday'], 'date': data[i]})

    return result, holiday_date
        

veg_day, holiday_date = check_day(data, holiday)
print(veg_day, '\n')
print(holiday_date)
