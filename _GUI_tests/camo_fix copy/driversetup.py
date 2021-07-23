from fake_useragent import UserAgent
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.utils import find_connectable_ip
from selenium.webdriver.support import expected_conditions as EC


# RUN CHROME DRIVER
def run_driver():
    options = uc.ChromeOptions()

    # setting profile
    options.user_data_dir = "c:\\temp\\profile"

    # another way to set profile is the below (which takes precedence if both variants are used
    options.add_argument('--user-data-dir=c:\\temp\\profile2')

    try:
        user_agent = UserAgent().random
        options.add_argument(f"user-agent={user_agent}")
    except:
        print("Bonding random UserAgent (Please Wait)")

    # options.add_argument("--incognito")

    # just some options passing in to skip annoying popups
    options.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    driver = uc.Chrome(options=options)

    return driver


# REDIRECT TO LINK
def redirect(driver, link):
    driver.get(link)


# CLEARS INPUT FIELD, THEN SENDS KEYS
def send_keys(element, keys):
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(keys)


# QUIT DRIVER
def quit_driver(driver, str=""):
    if (str != ""):
        print(str)
    # driver.quit()
