from selenium.webdriver.common.by import By
from pages.base_page import Page


class UserGuidePage(Page):
    USER_GUIDE_PAGE_TITLE = (By.CSS_SELECTOR, '.next-event-text')

    def verify_user_guide_page_opens(self):  # "User guide"
        self.wait_for_element_to_appear(*self.USER_GUIDE_PAGE_TITLE)