from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\commuter60\PycharmProjects\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)


# By ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'nav-cart-count')

# By XPATH

# Tag and attribute
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

# Multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

# By Xpath, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# Any tag = *
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

# Contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(), 't Seller') and @class='nav-a  ']")

# //parent[...]//child[...]
driver.find_element(By.XPATH, "//div[@id='nav-belt']//input[@placeholder='Search Amazon']")




# # ------------------------ HW2
# # --- Q1
# amazon_logo = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# email_field = driver.find_element(By.XPATH, "//input[@id='ap_email' and @name='email']")
# continue_button = driver.find_element(By.XPATH, "//input[@id='continue' and @class='a-button-input']")
# conditions_of_use_link = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
# privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
#
# need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#
# forgot_your_password_link = driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom' and @class='a-link-normal']")
# other_issues_link = driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and @class='a-link-normal']")
# create_your_amazon_acct_button = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit' and @class='a-button-text']")
#
# # ---Q2
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service(executable_path=r'C:\Users\commuter60\PycharmProjects\Drivers\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(service=service)
# driver.get("https://www.amazon.com")
# driver.maximize_window()
#
# # Click orders
# driver.find_element(By.XPATH, "//a[@id='nav-orders' and @href='/gp/css/order-history?ref_=nav_orders_first']").click()
#
# # Verifying sign in header
# expected_result = 'Sign in'
# actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
#
# assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
#
# # Verify email field present
# driver.find_element(By.XPATH, "//input[@id='ap_email']")
# print('Test case passed')
# driver.quit()