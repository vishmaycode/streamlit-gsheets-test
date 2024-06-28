import os
import streamlit as st
import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()
GSHEET_URL = os.environ.get("GSHEET_URL")

# Load credentials from JSON file
creds = Credentials.from_service_account_file(
    './gsheet-connect-service-account.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)

# Initialize the Google Sheets API client
client = gspread.authorize(creds)

# Function to fetch and display data from Google Sheets
def fetch_google_sheet_data():
    sheet_url = GSHEET_URL
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.get_worksheet(0)  # Assuming you want the first sheet

    # Fetch data from sheet
    data = worksheet.get_all_records()

    return data

# Main Streamlit app code
def main():
    st.title('Google Sheets Data Viewer')

    # Display instructions
    st.markdown("Click the button below to load data from your Google Sheet:")

    # Button to fetch data
    if st.button('Fetch Data'):
        data = fetch_google_sheet_data()

        # Display data in a table
        st.write("### Google Sheet Data")
        st.table(data)

# Run the app
if __name__ == '__main__':
    main()
