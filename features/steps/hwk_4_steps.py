# from behave import given, when, then
# from selenium.webdriver.common.by import By
#
# SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')
# SEARCH_RESULT = (By.CSS_SELECTOR, 'div.a-section.aok-relative.s-image-square-aspect')
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'span.a-button-inner input#add-to-cart-button')
# OPEN_CART_PAGE = (By.CSS_SELECTOR, ".a-button-text[href='/cart?ref_=sw_gtc")
# ACTUAL_RESULT = (By.CSS_SELECTOR, '#nav-cart-count')
# TOP_LINKS = (By.CSS_SELECTOR, '#CardInstanceKLjT_OYPP2HEViw5ELh5tg a')


# @given('Open Amazon BestSellers page')
# def open_bestsellers(context):
#     context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
#
#
# @then('Verify page has {expected_amount} links')
# def verify_link_amount(context, expected_amount):
#     expected_amount = int(expected_amount)
#     links = context.driver.find_elements(TOP_LINKS)
#     assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
#
#
# @when('Click search field')
# def click_search_field(context):
#     context.driver.find_element(*SEARCH_FIELD).click()
#
#
# @when('Look for {item}')
# def search_on_amazon(context, item):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(item)
#     context.driver.find_element(*SEARCH_BTN).click()
#
#
# @when('Click on the first result')
# def click_first_result(context):
#     context.driver.find_element(*SEARCH_RESULT).click()


# @when('Click on Add to Cart button')
# def click_add_to_cart_button(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()


# @when('Open cart page')
# def open_cart_page(context):
#     context.driver.find_element(*OPEN_CART_PAGE).click()


# @then('Verify result is {expected_result}')
# def verify_result(context,expected_result):
#     context.actual_result = context.driver.find_element(*ACTUAL_RESULT).text
#     assert expected_result == context.actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'