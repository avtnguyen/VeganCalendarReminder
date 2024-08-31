import os 
import json

# List of special holidays:
holiday = [{'holiday': 'tet nguyen dan', 'luna day': 1, 'luna month': 1}, {'holiday': 'tet nguyen dan', 'luna day': 2, 'luna month': 1}, 
           {'holiday': 'tet nguyen dan','luna day': 3, 'luna month' : 1}, {'holiday': 'tet nguyen dan', 'luna day': 4, 'luna month' : 1}, 
           {'holiday': 'tet nguyen tieu', 'luna day': 15, 'luna month' : 1}, {'holiday': 'tet han thuc', 'luna day': 3, 'luna month' : 3},
           {'holiday': 'gio to hung vuong', 'luna day': 10, 'luna month' : 3}, {'holiday': 'le phat dan', 'luna day': 15, 'luna month' : 4},
           {'holiday': 'tet doan ngo', 'luna day': 5, 'luna month' : 5}, {'holiday': 'le Vu Lan', 'luna day': 15, 'luna month' : 7},
           {'holiday': 'tet trung thu', 'luna day': 15, 'luna month' : 8}, {'holiday': 'le cung ong tao', 'luna day': 23, 'luna month' : 12}
        ]



# Function to check if the day is the 14th, 15th, the last day of each month and the first day of the next month
# in lunar calendar and if the day belong to the holiday list

def change_format_date(day_month, yr = 2024, isGregorian = True):
    if isGregorian :
        return f'{yr}-{day_month['month']}-{day_month['day']}'
    else:
        return f'{day_month['luna_month']}-{day_month['luna_day']}'
    
def check_day(data, holiday, yr):
    total_date = len(data)
    result = []
    holiday_date= []
    normal_summary = 'Vegan Day'
    for i in range(total_date):
        # check last and first day for each luna month:
        day_luna = int(data[i]['luna_day'])
        month_luna = int(data[i]['luna_month'])
        info = {'summary': normal_summary, 'day': change_format_date(data[i], yr, isGregorian = True),
                          'lunar day': change_format_date(data[i], yr, isGregorian=False )}
        if day_luna == 14 or day_luna == 15:
           result.append(info)
        elif i != 0 and day_luna == 1:
            prev_info = {'summary': normal_summary, 'day': change_format_date(data[i-1], yr, isGregorian = True),
                          'lunar day': change_format_date(data[i-1], yr, isGregorian=False )}
            result.append(prev_info)
            result.append(info)
        elif i == 0 and day_luna == 1:
            result.append(info)

        # check if date is in the holiday list:
        for j in range(len(holiday)):
            if day_luna == holiday[j]['luna day'] and month_luna == holiday[j]['luna month']: 
                holiday_info = {'summary': holiday[j]['holiday'], 'day': change_format_date(data[i], yr, isGregorian = True),
                          'lunar day': change_format_date(data[i], yr, isGregorian=False )}
                result.append(holiday_info)

    return result


# Read data json txt file:
for year in range(2017, 2031):

    data_file_path = 'data/processed/processed_' + str(year) + '.txt'
    with open(data_file_path) as data_file:
        data = json.load(data_file)

    veg_day = check_day(data, holiday, year)

    # Export processed data into the folder data/processed
    file_path_export = 'data/processed/' + 'vegan_day_' + str(year) +'.txt'

    with open(file_path_export,'w') as export_file:
        export_file.write(json.dumps(veg_day))

    print('Finish process file for {0} with file path {1}!'.format(year,file_path_export))




