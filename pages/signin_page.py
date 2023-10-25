from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    MAIN_PAGE_TITLE = (By.XPATH, "//div[@class='page-title']")
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BTN = (By.XPATH, "//a[@class='login-button w-button']")

    def open_signin_page(self):
        self.open_url('sign-in')

    def signin(self):
        self.input_text('mcneyo101@gmail.com', *self.EMAIL_INPUT)
        self.input_text('Ari53gdf7!*h', *self.PASSWORD_INPUT)
        self.wait_for_element_clickable_click(*self.CONTINUE_BTN)

        # Verify page title and and url after successful signin
    # def verify_signin_success(self):
    #     self.driver.find_element(*self.MAIN_PAGE_TITLE)
    #     self.verify_partial_url('.reelly.io/')
