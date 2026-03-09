import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import schedule
from datetime import datetime

# Get the absolute path to the HTML file in the same directory as this script
current_dir = os.path.dirname(os.path.abspath(__file__))
URL = f"file:///{os.path.join(current_dir, 'test_transmitter.html')}"

def read_transmitter():
    # --- BROWSER CONFIGURATION ---
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Make the browser invisible
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(URL)
        time.sleep(5) # Give the page JS time to randomize values

        # Read values (Selectors updated for more stability)
        forward_power = driver.find_element(By.XPATH, "//td[contains(text(),'FORWARD POWER')]/following::input[1]").get_attribute("value")
        reverse_power = driver.find_element(By.XPATH, "//td[contains(text(),'REVERSE POWER')]/following::input[1]").get_attribute("value")
        amp_voltage = driver.find_element(By.XPATH, "//td[contains(text(),'AMP VOLTAGE')]/following::input[1]").get_attribute("value")
        amp_current = driver.find_element(By.XPATH, "//td[contains(text(),'AMP CURRENT')]/following::input[1]").get_attribute("value")
        amp_temp = driver.find_element(By.XPATH, "//td[contains(text(),'AMP TEMPERATURE')]/following::input[1]").get_attribute("value")

        data = {
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Forward Power (W)": forward_power,
            "Reverse Power (W)": reverse_power,
            "Voltage (V)": amp_voltage,
            "Current (A)": amp_current,
            "Temperature (C)": amp_temp
        }

        df = pd.DataFrame([data])
        
        # Log to CSV
        log_file = "transmitter_log.csv"
        try:
            file_exists = os.path.isfile(log_file)
            df.to_csv(log_file, mode="a", header=not file_exists, index=False)
            print(f"[{data['Time']}] Data Logged Successfully.")
        except PermissionError:
            print(f"⚠️  WARNING: Could not save data. Please CLOSE 'transmitter_log.csv' in Excel!")

    except Exception as e:
        print(f"❌ Error during data collection: {e}")
    finally:
        driver.quit()

# --- TIMER CONFIGURATION ---
# Change the value below to adjust how often data is recorded.
# Options: .minutes, .hours, .days (examples: .every(30).minutes or .every(1).hours)
schedule.every(1).minutes.do(read_transmitter)

# Initial run to verify it works upon starting
print("Starting Transmitter Monitor...")
read_transmitter()

while True:
    try:
        schedule.run_pending()
        time.sleep(60)
    except KeyboardInterrupt:
        print("Stopping monitor...")
        break
