## Project Description

This project automates the task of creating events in Google Calendar as reminders for specific vegan days based on the lunar calendar and Vietnamese lunar calendar holidays. The vegan days are observed on the 14th, 15th, last, and first days of each month in the lunar calendar. These events will be set as reminders in the Gregorian calendar, making it easier to track important dates without manually calculating them.

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
2.Input the year
The script will prompt you to enter the year for which you want to import the vegan calendar. Enter the desired year in Gregorian format (e.g., 2024):

3.Event Creation
The script will automatically calculate the vegan days based on the Vietnamese lunar calendar and create events on the following days:

* 14th and 15th days of each lunar month
* Last day and 1st day of each lunar month
4. Check Google Calendar
Once the script completes, open your Google Calendar and verify that the vegan day reminders have been added on the appropriate Gregorian calendar dates.
