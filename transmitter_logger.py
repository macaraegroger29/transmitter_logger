import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import schedule
from datetime import datetime
import requests

# --- CONFIGURATION ---
URL = "http://192.168.1.14/index.shtml"

# --- TELEGRAM CONFIGURATION ---
BOT_TOKEN = "8561232630:AAE9MmFmcpp5G_SOdlsFqQwfPwOywjeKW-E"
CHAT_ID = "5393661292"

def send_telegram_message(message):
    if CHAT_ID == "5393661292":
        return # Skip if not configured
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"⚠️ Telegram Notify Failed: {e}")

def read_transmitter():
    # --- BROWSER CONFIGURATION ---
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Make the browser invisible
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(URL)
        time.sleep(3) # Give the page time to load

        # Read values using IDs from the live transmitter page
        forward_power = driver.find_element(By.ID, "mPf").get_attribute("value")
        reverse_power = driver.find_element(By.ID, "mPr").get_attribute("value")
        amp_voltage = driver.find_element(By.ID, "mVg").get_attribute("value")
        amp_current = driver.find_element(By.ID, "mIg").get_attribute("value")
        amp_temp = driver.find_element(By.ID, "mCg").get_attribute("value")

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
            
            success_msg = (
                f"📊 *Transmitter Data Logged*\n"
                f"Time: {data['Time']}\n"
                f"FWD: {data['Forward Power (W)']} W\n"
                f"REV: {data['Reverse Power (W)']} W\n"
                f"AMP Voltage: {data['Voltage (V)']} V\n"
                f"AMP Current: {data['Current (A)']} A\n"
                f"AMP Temp: {data['Temperature (C)']} °C"
            )
            print(f"[{data['Time']}] Data Logged Successfully.")
            send_telegram_message(success_msg)
        except PermissionError:
            print(f"⚠️  WARNING: Could not save data. Please CLOSE 'transmitter_log.csv' in Excel!")

    except Exception as e:
        error_msg = f"❌ Error during data collection: {e}"
        print(error_msg)
        send_telegram_message(error_msg)
    finally:
        driver.quit()

# --- TIMER CONFIGURATION ---
# Change the value below to adjust how often data is recorded.
# Options: .minutes, .hours, .days (examples: .every(30).minutes or .every(1).hours)
schedule.every(1).hours.do(read_transmitter)

# Initial run to verify it works upon starting
print("Starting Transmitter Monitor...")
send_telegram_message("🔌 Transmitter logger connected and monitoring...")
read_transmitter()

while True:
    try:
        schedule.run_pending()
        time.sleep(60)
    except KeyboardInterrupt:
        print("Stopping monitor...")
        break
