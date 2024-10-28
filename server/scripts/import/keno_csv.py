import csv
import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('lottery.sqlite')
cursor = conn.cursor()

# Define the game name
game_name = 'Keno'

# Define the correct path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), '../../data/Keno/formatted/2024.csv')

# Open the CSV file
with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        draw_date = row['PlayDate']
        draw_time = row['AP']
        numbers = ','.join([row[f'N{i:02}'] for i in range(1, 21)])

        try:
            cursor.execute('''
                INSERT INTO lottery_numbers (game_name, draw_date, draw_time, numbers)
                VALUES (?, ?, ?, ?)
            ''', (game_name, draw_date, draw_time, numbers))
        except sqlite3.IntegrityError:
            print(f"Duplicate entry for {game_name} on {draw_date} at {draw_time}")

# Commit and close the connection
conn.commit()
conn.close()