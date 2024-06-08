#!/usr/bin/env python3

# run_scripts.py

import subprocess

activate_command = "source ./.venv/Scripts/activate"  # Adjust the path
subprocess.run(activate_command, shell=True)


# Run script1.py
subprocess.run(["python", "scripts\scraper\Keno\webscraper.py"])

# Run script2.py
subprocess.run(["python", "scripts\scraper\Keno\cleandata.py"])

subprocess.run(["python", "scripts\scraper\Keno\order_csv.py"])
