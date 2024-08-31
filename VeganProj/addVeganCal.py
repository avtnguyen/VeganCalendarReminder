import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



def addToGoogleCalendar(calendar_name, event_description, date_start, date_end, 
                        first_reminder_type, first_reminder_time, 
                        second_reminder_type, second_reminder_time):
  """
  Add an all day event in google calendar using google calendar api
  """
  # If modifying these scopes, delete the file token.json.
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

    # Feature 3: add an event in the vegan calendar
    # Feature 3: Insert an event
    event = {
        'summary': calendar_name,
        
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
    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
    
    print(f"Created event: {created_event['id']}")
    
    
  except HttpError as error:
    print(f"An error occurred: {error}")

addToGoogleCalendar(calendar_name = 'Vegan Calendar', event_description = 'Test 4', 
                    date_start = '2024-08-31' , date_end = '2024-08-31', 
                        first_reminder_type = 'email', first_reminder_time = 3180, 
                        second_reminder_type = 'popup', second_reminder_time = 1740)


#if __name__ == "__main__":
#  main()