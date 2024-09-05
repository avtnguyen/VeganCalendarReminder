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

4. Run the script
After setting up the environment and Google Calendar API, run the project using:
```bash

python addVeganCal.py
```
