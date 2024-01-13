from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = '/home/bender/chromedriver'
chrome_service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
url = "https://www.surveyjunkie.com/member#!cp"
driver.get(url)

# Find the login element by link text (exact match)
login_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))

# Click the login element
login_element.click()

# Wait for the login page to load (adjust timeout as needed)
wait = WebDriverWait(driver, 10)
redirected_element_xpath = "//element-on-redirected-page"  # Replace with the actual XPath of an element on the redirected page
wait.until(EC.presence_of_element_located((By.XPATH, redirected_element_xpath)))

# Locate the email input field by its name attribute
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

# Clear any existing content in the email input field and type the email
email_input.clear()
email = "123224c@gmail.com"
email_input.send_keys(email)

# Continue with other interactions or actions

# Optional: Print the page source code
print(driver.page_source)

# Close the browser
driver.quit()