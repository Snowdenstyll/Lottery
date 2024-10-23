#!/usr/bin/env python3

# run_scraper.py

import subprocess
import os
import sys
import platform

def activate_venv():
    if platform.system() == "Windows":
        venv_path = os.path.join(os.getcwd(), '.venv', 'Scripts', 'activate.bat')
    else:
        venv_path = os.path.join(os.getcwd(), '.venv', 'bin', 'activate')

    if os.path.exists(venv_path):
        if platform.system() == "Windows":
            activate_command = f"call {venv_path} && "
        else:
            activate_command = f"source {venv_path} && "

        print("Activating virtual environment...")
        return activate_command
    else:
        print("Virtual environment not found. Please ensure it's set up correctly.")
        sys.exit(1)

def deactivate_venv():
    if platform.system() == "Windows":
        deactivate_command = "deactivate"
    else:
        deactivate_command = "deactivate"

    print("Deactivating virtual environment...")
    return deactivate_command

def run_script(script_path, activate_command):
    full_command = f"{activate_command}python {script_path}"
    try:
        subprocess.run(full_command, shell=True, check=True)
        print(f"Successfully ran {script_path}")
    except subprocess.CalledProcessError:
        print(f"Error occurred while running {script_path}")

if __name__ == "__main__":
    activate_command = activate_venv()

    # Install requests if not already installed
    subprocess.run(f"{activate_command}pip install requests", shell=True, check=True)

    script1_path = os.path.join(os.getcwd(), 'scripts', 'scraper', 'Keno', 'webscraper.py')
    run_script(script1_path, activate_command)

    script2_path = os.path.join(os.getcwd(), 'scripts', 'scraper', 'Keno', 'cleandata.py')
    run_script(script2_path, activate_command)

    script3_path = os.path.join(os.getcwd(), 'scripts', 'scraper', 'Keno', 'order_csv.py')
    run_script(script3_path, activate_command)

    deactivate_command = deactivate_venv()
    subprocess.run(deactivate_command, shell=True, check=True)