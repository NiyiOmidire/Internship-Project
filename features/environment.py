from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application


# def browser_init(context):

def browser_init(context, scenario_name):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    """
    # Google Chrome
    # service = Service(executable_path=r'C:\Users\commuter60\Desktop\Internship_Projects\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)

    # Other Browsers: Firefox
    # service = Service(executable_path=r'C:\Users\commuter60\Desktop\Internship_Projects\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    # Headless mode
    #
    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    # service = Service(executable_path=r'C:\Users\commuter60\Desktop\Internship_Projects\chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options = options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    ## Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'niyiomidire_SwJOJOb'
    bs_key = 'amypassswhat?5NcpYGhQsatp'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Sonoma',
        "debug": "true",
        'browserName': 'Chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # browser_init(context)
    # Pass scenario.name to init() for browserstack config:
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
