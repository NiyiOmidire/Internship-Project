from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

USER_GUIDE_VIDEOS = (By.CSS_SELECTOR, 'div[id="w-node-_4088696a-0a44-eb92-bc00-496f6787c12a-bfd82d00"] div.video-guide w-video w-embed')
# PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
# USER_GUIDE_PAGE_TITLE = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
VIDEO_TITLE = (By.CSS_SELECTOR, 'div.name-podcast')


@when('Click on User Guide option')
def click_user_guide(context):
    context.app.settings_page.click_on_user_guide()


@then('Verify the right page opens as {expected_result}')
def verify_right_page_opens(context, expected_result):
    context.app.user_guide_page.verify_user_guide_page_opens(expected_result)
@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.user_guide_page.verify_user_guide_page_opens()


@then('Verify all lesson videos contain titles')
def verify_videos_titles(context):
    all_videos = context.driver.find_elements(*USER_GUIDE_VIDEOS)

    for video in all_videos:
        video_title = video.find_element(*VIDEO_TITLE).text
        print(video_title)
        assert video_title, 'Video title not shown'

