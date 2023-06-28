# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START calendar_quickstart]
from __future__ import print_function

import datetime
import os.path

import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# new secret:
# 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
# Cl id: 593616687560-55nfvdqna3sadhe4jb605jlli77rphe8.apps.googleusercontent.com

def main():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    CREDENTIALS_FILE = 'cl_credentials.json'

    creds = None

    if os.path.exists('cl_token.json'):
        creds = Credentials.from_authorized_user_file('cl_token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)

        # Save the credentials for the next run
        with open('cl_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


if __name__ == '__main__':
    main()
