#combine all csv files in formated/ into one master csv file

import os
import csv
import re
import requests
from bs4 import BeautifulSoup
import operator
import datetime
import pandas as pd


date = datetime.datetime.now()
version = date.strftime("%y_%m_%d_%f")
csv_filename = f"data/LottoMax/master/{version}.csv"
csv_filename = "data/LottoMax/Master/master.csv"
output_directory = 'data/LottoMax/formatted/'
os.makedirs(output_directory, exist_ok=True)
header = ['PlayDate'] + [f'N{i:02d}' for i in range(1, 9)]
master_year_list = []

for year in range(2009, 2025):
    # File paths for the existing CSV files
    year_filename = os.path.join(output_directory, f'{year}.csv')
    with open(year_filename, newline='') as csvfile:
        year_csv = csv.reader(csvfile, quotechar='|')
        year_data  = list(year_csv)
        year_data .pop(0)
        master_year_list.extend(year_data)

length = len(list(master_year_list))

os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    for idx in range(length):
        row_data_year = master_year_list[idx]
        csv_writer.writerow(row_data_year)


df = pd.read_csv(csv_filename)

df['PlayDate'] = pd.to_datetime(df['PlayDate'])

# Sort the DataFrame by the 'PlayDate' column
df_sorted = df.sort_values(by=['PlayDate'])

# Save the sorted DataFrame to a new CSV file

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv(csv_filename, index=False)

print(f'The CSV file has been sorted by the "PlayDate" column and saved to {csv_filename}.')