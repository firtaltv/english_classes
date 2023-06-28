import os
import pickle

import googleapiclient.errors
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class CalendarManager:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.CREDENTIALS_FILE = 'classes/cl_credentials.json'
        self.service = self._get_calendar_service()

    def _get_calendar_service(self):
        creds = None

        if os.path.exists('classes/cl_token.pickle'):
            with open('classes/cl_token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIALS_FILE, self.SCOPES)
                creds = flow.run_local_server(port=8050)

            # Save the credentials for the next run
            with open('classes/cl_token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return build('calendar', 'v3', credentials=creds)

    def create_event(self, start_time, end_time, event_name):
        event_result = self.service.events().insert(
            calendarId="primary",
            body={
                "summary": event_name,
                "start": {"dateTime": start_time.isoformat(), "timeZone": "Europe/Kiev"},
                "end": {"dateTime": end_time.isoformat(), "timeZone": "Europe/Kiev"},
            }
        ).execute()

        return event_result['id']

    def update_event(self, start_time, end_time, eventid):
        self.service.events().patch(
            calendarId="primary",
            eventId=eventid,
            body={
                "start": {"dateTime": start_time.isoformat(), "timeZone": "Europe/Kiev"},
                "end": {"dateTime": end_time.isoformat(), "timeZone": "Europe/Kiev"},
            },
        ).execute()

    def delete_event(self, event_id):

        try:
            self.service.events().delete(
                calendarId='primary',
                eventId=event_id,
            ).execute()
        except googleapiclient.errors.HttpError:
            pass
