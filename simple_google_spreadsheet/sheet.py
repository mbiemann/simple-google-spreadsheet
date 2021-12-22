import pickle
import google_auth_oauthlib
from googleapiclient.discovery import build

class Sheet():

    def __init__(self, spreadsheet_id, client_id, client_secret):

        self._spreadsheet_id = spreadsheet_id

        credentials = google_auth_oauthlib.get_user_credentials(
            scopes=['https://www.googleapis.com/auth/spreadsheets'],
            client_id=client_id,
            client_secret=client_secret
        )

        self._service = build('sheets','v4',credentials=credentials).spreadsheets().values()
