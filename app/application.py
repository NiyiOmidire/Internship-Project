from pages.signin_page import SignInPage
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
# from pages.support_page import SupportPage
from pages.user_guide_page import UserGuidePage

class Application:

    def __init__(self, driver):
        self.signin_page = SignInPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.settings_page = SettingsPage(driver)
        self.user_guide_page = UserGuidePage(driver)