from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# the given precondition already exist in amazon_search_steps
# do not repeat the given behave will find it

#
# @when('Click orders')
# def click_orders(context):
#     context.driver.find_element(By.XPATH, "//a[@id='nav-orders' and @href='/gp/css/order-history?ref_=nav_orders_first']").click()
#
#
# @then('Verify sign in header')
# def verify_signin_header(context):
#     expected_result = 'Sign in'
#     actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
#     assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
#     # Verify email field present
#     context.driver.find_element(By.XPATH, "//input[@id='ap_email']")
#
#
# @when('Click cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()
#
#
# @then('Verify Amazon cart is empty')
# def verify_amazon_cart_empty(context):
#     expected_result = 'Your Amazon Cart is empty'
#     actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
#     assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
#
#
# @when('Click search Amazon field')
# def click_search_field(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox').click()
#
#
# @when('Search for lamp')
# def search_for_lamp(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox').send_keys('lamp')
#     context.driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button').click()
#
#
# @when('Click on the first product')
# def click_first_product(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'div.a-section.aok-relative.s-image-square-aspect').click()
#
#
# @when('Click on Add to Cart button')
# def click_add_to_cart_button(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'span.a-button-inner input#add-to-cart-button').click()
#
#
# @when('Open cart page')
# def open_cart_page(context):
#     # context.driver.find_element(By.CSS_SELECTOR, 'span#sw-gtc #sw-gtc_CONTENT.a-button-text').click()
#     context.driver.find_element(By.CSS_SELECTOR, ".a-button-text[href='/cart?ref_=sw_gtc']").click()
#
#
# @then('Verify cart has 1 item')
# def verify_cart_has_1_item(context):
#     expected_result = int(1)
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count')
#     assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'