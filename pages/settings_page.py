from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):
    USER_GUIDE_BTN = (By.LINK_TEXT, 'User guide')

    def click_on_user_guide(self):
        self.wait_for_element_clickable_click(*self.USER_GUIDE_BTN)



