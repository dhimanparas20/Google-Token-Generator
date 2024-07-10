from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import os
import configparser as cp
import json

# Read values from config.conf
config = cp.ConfigParser()
config.read('config.conf')

# Extract data from the DEFAULT section
client_id = config['GOOGLE'].get('CLIENT_ID')
client_secret = config['GOOGLE'].get('CLIENT_SECRET')
project_id = config['GOOGLE'].get('PROJECT_ID')
SCOPES = ['https://www.googleapis.com/auth/drive.file']

#########################
#       HOW TO USE
#########################
# Import this method in your main code
# Create config.json file having the following vars with values filled
'''
[GOOGLE]
CLIENT_ID = 
CLIENT_SECRET = 
PROJECT_ID = 
USE_SERVICE_ACCOUNTS =
GDRIVE_FOLDER_ID = 
'''
# REMEBER TO RUN THIS CODE on LOCAL MACHINE ONLY & NOT ON REMOTE MACHINE
# call writeCredentialsJson() to create credentails.json
# call genTokenJson() to create token.json
# Store the returned value from above code.
# Thats it, credentials.json and token.json files will be generated


#create Credenstials.json
def writeCredentialsJson():
    # Prepare data to be written to credentials.json
    data = {"installed":
            {
                "client_id":client_id,
                "project_id":project_id,
                "auth_uri":"https://accounts.google.com/o/oauth2/auth",
                "token_uri":"https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":client_secret,
                "redirect_uris":["localhost"]
            }
        }   

    # Write data to credentials.json
    with open('credentials.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Generate token.json
def genTokenJson():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
