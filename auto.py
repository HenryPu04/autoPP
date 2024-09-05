from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

# Initialize WebDriver
driver = webdriver.Safari()  
# Open Discord 
driver.get('https://discord.com/channels/946247465168945172/960713285034999818')
# Wait for the page to load fully
time.sleep(7)
# Regular expression to match PrizePicks links
prizepicks_pattern = re.compile(r"https://prizepicks\.onelink\.me/gCQS/shareEntry\?entryId=\S*")
# Retrieve all messages in the channel (adjust the CSS selector based on Discord's structure)
messages = driver.find_elements(By.CSS_SELECTOR, '.messageContent-2qWWxC')
# Search for PrizePicks links in the messages
for message in messages:
    content = message.text
    prizepicks_links = prizepicks_pattern.findall(content)
    if prizepicks_links:
        for link in prizepicks_links:
            print(f"Found PrizePicks link: {link}")
            # Optionally, trigger the bet submission process using Selenium
            # submit_prizepicks_bet(link)
# Close the browser when done
driver.quit()


