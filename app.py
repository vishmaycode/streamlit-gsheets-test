import os
import streamlit as st
import gspread
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
# def fetch_google_sheet_data():
#     sheet_url = GSHEET_URL
#     sheet = client.open_by_url(sheet_url)
#     worksheet = sheet.get_worksheet(0)  # Assuming you want the first sheet

#     # Fetch data from sheet
#     data = worksheet.get_all_records()

#     return data

# Function to add a row to Google Sheets
def add_row_to_google_sheet(new_row, worksheet_name):
    sheet_url = GSHEET_URL
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.worksheet(worksheet_name)

    # Append the new row to the bottom of the sheet
    worksheet.append_row(new_row)

# Main Streamlit app code
def main():
    st.title('Test Badminton Form')

    # # Section to add a new row
    # st.header("Add a New Row")

    # Create input fields for the new row data
    new_row = {}
    new_row['Player Name'] = st.text_input("Player Name:")
    new_row['State ID Number'] = st.text_input("State ID Number:")
    new_row['Mobile Number'] = st.text_input("Mobile Number:")
    new_row['Gender'] = st.radio("Gender:", ["Male", "Female"])
    new_row['Training Centre'] = st.selectbox("Training Centre:", [
        "", "RCC Panjim", "RCC Mapusa", "Khelo India Centre Campal",
        "Salvador De Mundo", "Chicalim", "Don Boasco Oratory",
        "Panjim Gymkhana", "Gaspar Diass Miramar", "Other"
    ])

    st.write("Categories Participating in:")
    if new_row['Gender']:
       new_row['Singles'] = st.checkbox("Singles")
       new_row['Doubles'] = st.checkbox("Doubles")
       new_row['Mixed Doubles'] = st.checkbox("Mixed Doubles")
   
       new_row['Singles'] = "Singles" if new_row['Singles'] else "-"
       new_row['Doubles'] = "Doubles" if new_row['Doubles'] else "-"
       new_row['Mixed Doubles'] = "Mixed Doubles" if new_row['Mixed Doubles'] else "-"

    if new_row['Doubles'] == "Doubles":
        new_row['Doubles Partner'] = st.text_input("Name of Doubles Partner:")
        new_row['State ID Number of Doubles'] = st.text_input("State ID of Doubles Partner:")
    else:
        new_row['Doubles Partner'] = "-"
        new_row['State ID Number of Doubles'] = "-"
    
    if new_row['Mixed Doubles'] == "Mixed Doubles":
        new_row['Mixed Doubles Partner'] = st.text_input("Name of Mixed Doubles Partner:")
        new_row['State ID Number of Mixed Doubles'] = st.text_input("State ID Number of Mixed Doubles")
        # # Set default gender for mixed doubles partner
        # default_partner_gender = "Male" if new_row['Gender'] == "Female" else "Female"
        # new_row['Mixed Doubles Partner'] = st.text_input("Name of Mixed Doubles Partner:")
        # new_row['State ID Number of Mixed Doubles'] = st.text_input(
        #     f"State ID of Mixed Doubles Partner ({default_partner_gender}):"
        # )
    else:
        new_row['Mixed Doubles Partner'] = "-"
        new_row['State ID Number of Mixed Doubles'] = "-"

        # Button to add the new row
    if st.button('Submit'):
            # Check if mandatory fields are filled
        if not new_row['Player Name'] or not new_row['State ID Number'] or not new_row['Mobile Number'] or not new_row['Gender']:
            st.error("Please fill in all the mandatory fields.")
        else:
                # Prepare data for submission
            if new_row['Gender'] == "Male":
                if new_row['Singles']:
                    Singles_row = [
                        new_row['Player Name'],
                        new_row['State ID Number'],
                        new_row['Mobile Number'],
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Singles']
                    ]
                    add_row_to_google_sheet(Singles_row, 'Sheet1')

                # Add doubles partners to their respective sheets if applicable
                # Split the main data into two parts
                if new_row['Doubles'] == "Doubles":
                    first_half_row = [
                        new_row['Player Name'],
                        new_row['State ID Number'],
                        new_row['Mobile Number'],
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Doubles']
                    ]
                    second_half_row = [
                        new_row['Doubles Partner'],
                        new_row['State ID Number of Doubles'],
                        "",
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Doubles']
                    ]
                # Add to the doubles sheet
                    add_row_to_google_sheet(first_half_row, 'Sheet2')
                    add_row_to_google_sheet(second_half_row, 'Sheet2')
            
                # Add mixed doubles partners to their respective sheets if applicable
                # Split the main data into two parts
                if new_row['Mixed Doubles'] == "Mixed Doubles":
                    first_half_row = [
                        new_row['Player Name'],
                        new_row['State ID Number'],
                        new_row['Mobile Number'],
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Mixed Doubles']
                    ]
                    second_half_row = [
                        new_row['Mixed Doubles Partner'],
                        new_row['State ID Number of Mixed Doubles'],
                        "",
                        "Female",
                        new_row['Training Centre'],
                        new_row['Mixed Doubles']
                    ]
                # Add to the mixed doubles sheet
                    add_row_to_google_sheet(first_half_row, 'Sheet3')
                    add_row_to_google_sheet(second_half_row, 'Sheet3')

            elif new_row['Gender'] == "Female":
                if new_row['Singles']:
                    Singles_row = [
                        new_row['Player Name'],
                        new_row['State ID Number'],
                        new_row['Mobile Number'],
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Singles']
                    ]
                    add_row_to_google_sheet(Singles_row, 'Sheet4')

                 # Add doubles partners to their respective sheets if applicable
                # Split the main data into two parts
                if new_row['Doubles'] == "Doubles":
                    first_half_row = [
                        new_row['Player Name'],
                        new_row['State ID Number'],
                        new_row['Mobile Number'],
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Doubles']
                    ]
                    second_half_row = [
                        new_row['Doubles Partner'],
                        new_row['State ID Number of Doubles'],
                        "",
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Doubles']
                    ]
                # Add to the doubles sheet
                    add_row_to_google_sheet(first_half_row, 'Sheet5')
                    add_row_to_google_sheet(second_half_row, 'Sheet5')
            
                # Add mixed doubles partners to their respective sheets if applicable
                # Split the main data into two parts
                if new_row['Mixed Doubles'] == "Mixed Doubles":
                    first_half_row = [
                        new_row['Player Name'],
                        new_row['State ID Number'],
                        new_row['Mobile Number'],
                        new_row['Gender'],
                        new_row['Training Centre'],
                        new_row['Mixed Doubles']
                    ]
                    second_half_row = [
                        new_row['Mixed Doubles Partner'],
                        new_row['State ID Number of Mixed Doubles'],
                        "",
                        "Male",
                        new_row['Training Centre'],
                        new_row['Mixed Doubles']
                    ]
                # Add to the mixed doubles sheet                  
                    add_row_to_google_sheet(second_half_row, 'Sheet3')
                    add_row_to_google_sheet(first_half_row, 'Sheet3')

                 
            st.success("Submitted Successfully!")

#    # Button to add the new row
#     if st.button('Submit'):
#         # Check if mandatory fields are filled
#         if not new_row['Player Name'] or not new_row['State ID Number'] or not new_row['Mobile Number'] or not new_row['Gender']:
#             st.error("Please fill in all the mandatory fields.")
#         else:
#             # Add to the main sheet
#             main_row = [
#                 new_row['Player Name'],
#                 new_row['State ID Number'],
#                 new_row['Mobile Number'],
#                 new_row['Gender'],
#                 new_row['Training Centre'],
#                 new_row['Singles']
#                 # new_row['Doubles'],
#                 # new_row['Mixed Doubles'],
#                 # new_row['Doubles Partner'],
#                 # new_row['State ID Number of Doubles'],
#                 # new_row['Mixed Doubles Partner'],
#                 # new_row['State ID Number of Mixed Doubles']
#             ]
#             add_row_to_google_sheet(main_row, 'Sheet1')

#             # Add doubles and mixed doubles partners to their respective sheets if applicable
#             if new_row['Doubles'] == "Doubles":
#                 doubles_row = [
#                     # new_row['Player Name'],
#                     new_row['Doubles Partner'],
#                     new_row['State ID Number of Doubles']
#             ]
#             add_row_to_google_sheet(doubles_row, 'Sheet2')

#             if new_row['Mixed Doubles'] == "Mixed Doubles":
#                 mixed_doubles_row = [
#                     new_row['Player Name'],
#                     new_row['Mixed Doubles Partner'],
#                     new_row['State ID Number of Mixed Doubles']
#                 ]
#                 add_row_to_google_sheet(mixed_doubles_row, 'Sheet3')

#             st.success("Submitted Successfully!")

# Run the app
if __name__ == '__main__':
    main()
