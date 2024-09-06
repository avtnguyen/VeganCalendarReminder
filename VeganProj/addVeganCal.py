import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




  # If modifying these scopes, delete the file token.json.
calendar_name = 'Vegan Calendar'
SCOPES = ["https://www.googleapis.com/auth/calendar"]
creds = None

  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
if os.path.exists("../../credential/vegan_token.json"):
    creds = Credentials.from_authorized_user_file("../../credential/vegan_token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
          "../../credential/google_calendar_credential.json", SCOPES
      )
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
with open("../../credential/vegan_token.json", "w") as token:
    token.write(creds.to_json())
try:
    service = build("calendar", "v3", credentials=creds)
except HttpError as error:
    print(f"An error occurred: {error}")


    # Feature 1: Check if vegan calendar is in the list, if not add the new calendar
    #vegan_calendar = 'Vegan Calendar'
print("Fetching all calendars:")
calendar_list = service.calendarList().list().execute().get('items', [])
flag = False
for calendar in calendar_list:
    if calendar['summary'] == calendar_name:
        flag = True
        calendar_id = calendar['id']
    print(calendar['summary'])

# Feature 2: Create a new calendar
if flag == False:
    new_calendar = {
        'summary': calendar_name,
        'timeZone': 'America/Toronto'
    }
    created_calendar = service.calendars().insert(body=new_calendar).execute()
    calendar_id = created_calendar['id']
    print(f"Created calendar: {calendar_id}")
else:
    print(f'Calendar {calendar_name} is alread exist!')

# add an all-day event in the vegan calendar

def addToGoogleCalendar(event_description: str, date_start: str, date_end: str, 
                        first_reminder_type: str, first_reminder_time: int, 
                        second_reminder_type: str, second_reminder_time: int, 
                        calendar_ID, service):
    '''
    event_description: string describe the event
    date_start: string with format yyyy-mm-dd
    end_start: string with format yyyy-mm-dd
    first_reminder_type: string with options 'email' or 'popup'
    first_reminder_time: int showing number minutes before the event
    second_reminder_type: string with options 'email' or 'popup'
    second_reminder-time: int showing number of minutes before the event
    calendar_ID: id of the chosen calendar obtain from google api
    service: service object from google api
    '''
    
    
    
    event = {
        'summary': event_description,
        
        'description': event_description,
        'start': {
            'date': date_start,
            'timeZone': 'America/Toronto',
        },
        'end': {
            'date': date_end,
            'timeZone': 'America/Toronto',
        },
        'reminders':{
            "useDefault": False,
            "overrides": [
            {
                "method": first_reminder_type,
                "minutes": first_reminder_time #3180
            },
            {
               "method": second_reminder_type,
                "minutes": second_reminder_time #1740
            }]
        }
    }
    created_event = service.events().insert(calendarId=calendar_ID, body=event).execute()
    
    print(f"Created event: {event_description} with id {created_event['id']}")
    

    
if __name__ == "__main__":
    
    inputYear = int(input('Please give the year to import the vegan calendar ranging from 2017 to 2030:'))
    while True:
        if inputYear >= 2017 and inputYear <= 2030:
            break
        else:
            inputYear = int(input('Please give the year to import the vegan calendar ranging from 2017 to 2030:'))
            
    data_file_path = 'data/processed/vegan_day_' + str(inputYear) + '.txt'
    with open(data_file_path) as data_file:
        vegan_day = json.load(data_file)

    for day in vegan_day:
        
        description =f"{day['summary']}. Lunar day: {day['lunar day']}. Gregorian day: {day['day']}" 
        
        addToGoogleCalendar(event_description = description, 
                    date_start = day['day'] , date_end = day['day'], 
                        first_reminder_type = 'email', first_reminder_time = 3180, 
                        second_reminder_type = 'popup', second_reminder_time = 1740, 
                        calendar_ID = calendar_id, service = service)