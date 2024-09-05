from selenium import webdriver
import time

# Initialize Safari WebDriver
driver = webdriver.Safari()

# Wait for the browser to open fully
time.sleep(5)

# Now try opening the Discord URL
driver.get('https://www.google.com')

# Wait for a few seconds to observe the behavior
time.sleep(10)

# Optionally, close the browser
driver.quit()

