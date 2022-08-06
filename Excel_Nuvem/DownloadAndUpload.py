import secrets
import os 
import io 

from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
from xmlrpc.client import SERVER_ERROR
from Google import Create_Service
from googleapiclient.errors import HttpError

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME           = 'drive'
API_VERSION        = 'v3'
SCOPES             = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def download_file(real_file_id):

    try:
        file_id = real_file_id
        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.getvalue()

def get_file(file_id, file_directory):
    download = download_file(file_id)
    with open(file_directory, "wb")  as f: 
        f.write(download)
        f.close()

def upload_file(file_directory, file_id): 
    media = MediaFileUpload(file_directory, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    file = service.files().update(fileId=file_id,
                                 media_body=media).execute()


