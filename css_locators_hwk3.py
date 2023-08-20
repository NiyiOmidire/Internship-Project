import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\commuter60\PycharmProjects\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList-nav-line-1').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()
time.sleep(3)

# Amazon logo
# driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account button
# driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')

# Your name field
# driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Mobile number or email field
# driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

# password field
# driver.find_element(By.CSS_SELECTOR, 'input#ap_password')

# Password must be at least 6 text
# driver.find_element(By.CSS_SELECTOR, 'div.auth-inlined-information-message.a-alert-inline div.a-alert-content')

# Re-enter password field
# driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

# Continue button
# driver.find_element(By.CSS_SELECTOR, 'input#continue')

# condition of use link
# driver.find_element(By.CSS_SELECTOR, 'a[href*="notification_condition_of_use"]')

# Privacy Notice link
# driver.find_element(By.CSS_SELECTOR, 'a[href*="/display.html/ref=ap_register_notification_privacy_notice"]')

# Sign in link
# driver.find_element(By.CSS_SELECTOR, 'a[href*="ap/signin?openid.pape.max_auth_age=0&openid.return_to"]')
