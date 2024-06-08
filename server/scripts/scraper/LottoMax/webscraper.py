## STEP 1
# Get the data from site and save it to csv file
##

import requests
import csv
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pandas as pd

years = ['2009', '2010', '2011', '2012', '2013', '2014','2015', '2016', '2017', '2018', '2019', '2020', '2021','2022', '2023', '2024']
#years = ['2023']
#year = '2024'

#for year in years:

def getDates (dates):
    date_elements = []
    for tr in dates:
        first_td = tr.find('td')  # Find the first 'td' element in the 'tr'
        if first_td:
            date_elem = re.sub(r'[^a-zA-Z0-9 ]', '', first_td.text.strip())
            if date_elem != "":
                date_element = datetime.strptime(date_elem, "%B %d %Y").strftime("%Y-%m-%d")
                date_elements.append(date_element)

    return date_elements

def getNumbers (winning_numbers):
    winning_numbers_arr = []
    for wn in winning_numbers:
        numbers = wn.find_all('div', class_='number')
        winning_numbers_arr.append([num.text for num in numbers])
    return winning_numbers_arr

for year in range(2009, 2025):
    URL = f"https://www.lotteryleaf.com/lotto-max/{year}"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    winning_numbers = soup.find_all('div', class_='c-lottery-numbers')
    winning_numbers_arr = getNumbers(winning_numbers)

    dates = soup.find('table').find_all('tr')
    dates_arr = getDates(dates)
    #print(dates_arr)

    if winning_numbers:
        csv_filename = f"data/LottoMax/scraping/extracted_numbers_{year}.csv"
        header = ['PlayDate'] + [f'N{i:02d}' for i in range(1, 9)]
        with open(csv_filename, 'w+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(header)
            for idx, winning_number in enumerate(winning_numbers_arr):
                date_element = dates_arr[idx]
                print(winning_number)
                row_data = [date_element] + winning_number  # Assuming winning_number is a space-separated string
                # Write the row to the CSV file
                csv_writer.writerow(row_data)
        print(f"Writing to CSV file complete -{year}")

    else:
        print("No ul element found with class 'nbr-grp'.")


for year in range(2009, 2025):
    csv_filename = f"data/LottoMax/formatted/{year}.csv"

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)

    df['PlayDate'] = pd.to_datetime(df['PlayDate'])

    # Sort the DataFrame by the 'PlayDate' column
    df_sorted = df.sort_values(by=['PlayDate'])

    # Save the sorted DataFrame to a new CSV file

    # Save the sorted DataFrame to a new CSV file
    df_sorted.to_csv(csv_filename, index=False)

    print(f'The CSV file has been sorted by the "PlayDate" column and saved to {csv_filename}.')