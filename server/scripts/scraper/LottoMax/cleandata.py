# STEP 2
# Combines the midday and evening csv files into one csv file
# placed in the formatted/{year}.csv file

import os
import csv
import re
import requests
import operator
from bs4 import BeautifulSoup
import operator
import pandas as pd

year='2024'

# Your existing code...
if year == '2019':
    exit()

# Ensure the directories exist, create them if not
output_directory = 'data/LottoMax/scraping/'
os.makedirs(output_directory, exist_ok=True)

for year in range(2009, 2025):
    # File paths for the existing CSV files
    filename = os.path.join(output_directory, f'extracted_numbers_{year}.csv')

    # Determine the starting 'AP' for the new CSV file

    evening_list = list

    with open(filename, newline='') as csvfile:
        evening_csv = csv.reader(csvfile, quotechar='|')
        evening_list = list(evening_csv)
        evening_list.pop(0)

    length = len(list(evening_list))

    csv_filename = f"data/LottoMax/formatted/{year}.csv"
    header = ['PlayDate'] + [f'N{i:02d}' for i in range(1, 9)]

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)
        index_balancer = 0
        for idx in range(length):
            row_data_evening = evening_list[idx - index_balancer]
            csv_writer.writerow(row_data_evening)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)

    df['PlayDate'] = pd.to_datetime(df['PlayDate'])

    # Sort the DataFrame by the 'PlayDate' column
    df_sorted = df.sort_values(by=['PlayDate'])

    # Save the sorted DataFrame to a new CSV file
    df_sorted.to_csv(csv_filename, index=False)

    print(f'The CSV file has been sorted by the "PlayDate" column and saved to {csv_filename}.')
