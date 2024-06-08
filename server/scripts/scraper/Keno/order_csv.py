# Step 3
# order a single csv file by date and ap

import os
import csv
import re
import requests
import operator
from bs4 import BeautifulSoup
import operator
import pandas as pd

year = '2024'

csv_filename = f"data/Keno/formatted/{year}.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_filename)

df['PlayDate'] = pd.to_datetime(df['PlayDate'])

# Sort the DataFrame by the 'PlayDate' column
df_sorted = df.sort_values(by=['PlayDate','AP'])

# Save the sorted DataFrame to a new CSV file

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv(csv_filename, index=False)

print(f'The CSV file has been sorted by the "PlayDate" column and saved to {csv_filename}.')