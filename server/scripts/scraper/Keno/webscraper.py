##
# Step 1
# Get the data from site and save it to csv file
##

import requests
import csv
from bs4 import BeautifulSoup
import re
from datetime import datetime


#type ='am'
year = '2024'

Time_AM = {
    "code": "A",
    "label": "midday",
}

Time_PM = {
    "code": "P",
    "label": "evening",
}

Times = {'am' : Time_AM, 'pm' : Time_PM}

time_sets = ['am', 'pm']

if (year == '2019'):
    exit()


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
        winning_numbers_arr.append(wn.text.split())
    return winning_numbers_arr

for t in time_sets:
    type = t
    URL = f"https://www.lotteryleaf.com/on/on-daily-keno-{Times[type]['label']}/{year}"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    winning_numbers = soup.find_all('div', class_='c-lottery-numbers')
    winning_numbers_arr = getNumbers(winning_numbers)

    dates = soup.find('table').find_all('tr')
    dates_arr = getDates(dates)

    if winning_numbers:
        csv_filename = f"data/Keno/scraping/extracted_numbers_{Times[type]['label']}_{year}.csv"
        header = ['PlayDate', 'AP'] + [f'N{i:02d}' for i in range(1, 21)]
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(header)
            for idx, winning_number in enumerate(winning_numbers_arr):
                date_element = dates_arr[idx]
                row_data = [date_element] + [Times[type]['code']] + winning_number  # Assuming winning_number is a space-separated string
                # Write the row to the CSV file
                csv_writer.writerow(row_data)
        print(f"Writing to CSV file complete -{year} {Times[type]['label']}")

    else:
        print("No ul element found with class 'nbr-grp'.")

