# Step 4
# combine all csv files in formated/ into one master csv file

import os
import csv
import re
import requests
from bs4 import BeautifulSoup
import operator
import datetime

years = ['2019', '2020', '2021', '2022', '2023', '2024']

date = datetime.datetime.now()
version = date.strftime("%y_%m_%d_%f")
csv_filename = f"data/Keno/master/{version}.csv"
output_directory = 'data/Keno/formatted/'
os.makedirs(output_directory, exist_ok=True)
header = ['PlayDate', 'AP'] + [f'N{i:02d}' for i in range(1, 21)]
master_year_list = []

for year in years:
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