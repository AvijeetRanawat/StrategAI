import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

L = "https://fbref.com/en/squads/822bd0ba/Liverpool-Stats"
M = 'https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats'

# Replace with the actual URL
url = L

# Send a GET request to the page
response = requests.get(url)


# Function to merge the column headers with the first row of data
def merge_headers_with_first_row(df):
    # Extract the first row of data
    # first_row = df.iloc[0]

    # Create new column headers
    new_headers = []
    for header in df.columns:
        # Join tuple elements with a space and make it a string, then check for 'unnamed'
        if isinstance(header, tuple):
            if 'unnamed' not in header[0].lower():
                new_header = ' '.join(header)
            else:
                new_header = ' '.join(header[1:])
        # header_str = ' '.join(header) if isinstance(header, tuple) else str(header)
        # if 'unnamed' not in header_str.lower():
        #     new_header = f"{header_str} {data}"
        # else:
        #     new_header = data
        new_headers.append(new_header)

    # Replace the current headers with the new headers
    df.columns = new_headers


    # # Drop the first row from the DataFrame
    # df = df.drop(df.index[0])

    # Reset the DataFrame index
    df.reset_index(drop=True, inplace=True)

    return df



# Check if the request was successful
if response.status_code == 200:
    # Use BeautifulSoup to parse the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table on the page
    # You might need to adjust this selector to match the page structure
    table = soup.find('table')

    # Convert the table to a string and wrap in a StringIO object
    table_io = StringIO(table.prettify())

    # Read the HTML table into a pandas DataFrame
    df = pd.read_html(table_io)[0]

    # Drop the last two rows of the DataFrame
    df_dropped_rows = df.iloc[:-2]

    # Drop the last column of the DataFrame
    df_final = df_dropped_rows.iloc[:, :-1]

    # Use the function and pass the DataFrame to it
    df_final = merge_headers_with_first_row(df_final)

    # Calculate the threshold for non-NaN values that must be present to keep the row
    # If more than 70% are NaN, the row will be dropped
    threshold = len(df_final.columns) * 0.3  # 30% non-NaN values

    # Drop rows where the number of non-NaN values is less than the threshold
    df_final = df_final.dropna(thresh=threshold)

    # Save the DataFrame to a CSV file
    df_final.to_csv('liverpool_stats.csv', index=False)
else:
    print('Failed to retrieve the webpage')