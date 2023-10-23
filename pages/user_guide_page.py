from selenium.webdriver.common.by import By
from pages.base_page import Page


class UserGuidePage(Page):
    USER_GUIDE_PAGE_TITLE = (By.CSS_SELECTOR, 'div.next-event-text')

    def verify_user_guide_page_opens(self, expected_result):  # "User guide"
        self.verify_text(expected_result, *self.USER_GUIDE_PAGE_TITLE)