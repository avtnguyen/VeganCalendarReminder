## Project Description

This project automates the task of creating events in Google Calendar as reminders for specific vegan days based on the lunar calendar and Vietnamese lunar calendar holidays. The vegan days are observed on the 14th, 15th, last, and first days of each month in the lunar calendar. These events will be set as reminders in the Gregorian calendar, making it easier to track important dates without manually calculating them.

## Prerequisites
- Python 3.x
- Google Calendar API
- Required Python libraries (listed in `requirements.txt`)

## Installation Instructions

To set up and run this project, follow these steps:

1. **Clone the repository**  
   Download or clone the project repository to your local machine:
   ```bash
   git clone https://github.com/avtnguyen/VeganCalendarReminder
2. Install required packages
Ensure you have the necessary Python libraries installed by running:
```bash
pip install -r requirements.txt
```
3. Set up Google Calendar API
To integrate the Google Calendar API:

Visit the Google Cloud Console.
Create a new project or use an existing one.
Enable the Google Calendar API for your project.
Generate OAuth 2.0 credentials and download the credentials.json file.
Save the credentials.json file as "google_calendar_credential.json" in the directory 'credential' of your project.

## Usage
After installing the project and setting up the Google Calendar API, follow these steps to create reminders for vegan days:

1. **Run the script**  
   Execute the script to begin the process of generating vegan day reminders:
   ```bash
   python addVeganCal.py
   ```
2. **Input the year**
The script will prompt you to enter the year for which you want to import the vegan calendar. Enter the desired year in Gregorian format (e.g., 2024):

3. **Event Creation**
The script will automatically calculate the vegan days based on the Vietnamese lunar calendar and create events on the following days:

* 14th and 15th days of each lunar month
* Last day and 1st day of each lunar month
  
4. **Check Google Calendar**
Once the script completes, open your Google Calendar and verify that the vegan day reminders have been added on the appropriate Gregorian calendar dates.

## Code Explanation

This project utilizes the Google Calendar API and Python to perform web scraping of the Vietnamese lunar calendar and automatically create calendar events. Below is an overview of the project's main scripts:

- `scraper.py`: This script performs web scraping from [xemlicham.com](https://www.xemlicham.com/am-lich/nam/) and downloads the raw lunar calendar data from the website.
- `parser.py`: This script processes the raw data obtained from the web scraping, converting it into a structured JSON file that contains the lunar calendar dates and their corresponding Gregorian calendar dates, covering the years 2017 to 2030.
- `selectVeganDay.py`: This script identifies the vegan days and Vietnamese lunar holidays based on the parsed data and outputs the selected dates in a JSON format like:  
  `{"summary": "Vegan Day", "day": "2017-12-18", "lunar day": "11-1"}`
- `addVeganCal.py`: This script uses the Google Calendar API to add the selected vegan days and lunar holidays as events to the user's Google Calendar.

## Results
After running the project, the following events are created in your Google Calendar:
- Vegan days on the 14th, 15th, last, and 1st days of each lunar month.
- Vietnamese lunar holidays
  
## Limitations
- The project only supports the Vietnamese lunar calendar.
- The vegan days are based on specific rules that might not apply to all lunar-based traditions.

## Future Work
- Add functionality to customize the event times and reminders.

