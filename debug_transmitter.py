from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

URL = "http://192.168.1.14/index.shtml"

def debug_scrape():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    try:
        print(f"Connecting to {URL}...")
        driver.get(URL)
        time.sleep(5)
        
        print("\n--- PAGE TITLE ---")
        print(driver.title)

        print("\n--- ATTEMPTING TO FIND LABELS (Case Insensitive) ---")
        labels = ["FORWARD POWER", "REVERSE POWER", "AMP VOLTAGE", "AMP CURRENT", "AMP TEMPERATURE"]
        
        for label in labels:
            print(f"\nSearching for label: '{label}'")
            # Try finding any element containing the text
            elements = driver.find_elements(By.XPATH, f"//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{label.lower()}')]")
            if not elements:
                print(f"  X No element found containing '{label}'")
                continue
                
            for i, el in enumerate(elements):
                print(f"  Found '{label}' in <{el.tag_name}> tag.")
                # Try to find an input or text nearby
                try:
                    # Look for input nearby
                    nearby_input = el.find_element(By.XPATH, "./following::input[1]")
                    print(f"    - Found nearby <input> value: '{nearby_input.get_attribute('value')}'")
                except:
                    pass
                
                try:
                    # Look for text in next sibling td
                    next_td = el.find_element(By.XPATH, "./following-sibling::td[1]")
                    print(f"    - Found next <td> text: '{next_td.text.strip()}'")
                except:
                    pass

        print("\n--- FULL PAGE SOURCE SNAPSHOT (First 1000 chars) ---")
        print(driver.page_source[:1000])
        
        # Save full source to a file for me to read
        with open("transmitter_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("\n✅ Full page source saved to 'transmitter_source.html'")

    except Exception as e:
        print(f"❌ Debug Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_scrape()
