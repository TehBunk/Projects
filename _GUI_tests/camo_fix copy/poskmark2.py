import re
import os
import time
import random
import string
import urllib.request


from vardata import *
from driversetup import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


LINK = "https://poshmark.com/"
CHROME_DRIVER = None


class Poshmark():
    def __init__(self):
        global CHROME_DRIVER

        CHROME_DRIVER = run_driver()
        self.login()
        self.get_user_info()
        self.search_for_term()
        self.follow_users_recursive()
        time.sleep(100)

    def login(self):
        self.check_running_wait()
        redirect(CHROME_DRIVER, link=(LINK + "login"))

        try:  # FIND USERNAME & PASSWORD INPUTS (ALSO LOGIN BUTTON)
            input_username_login = WebDriverWait(CHROME_DRIVER, 3).until(
                EC.presence_of_element_located((By.ID, "login_form_username_email")))
            input_password_login = WebDriverWait(CHROME_DRIVER, 3).until(
                EC.presence_of_element_located((By.ID, "login_form_password")))
            button_login = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn--primary blue btn-primary']")))
        except:  # COULD NOT FIND INPUTS
            quit_driver(CHROME_DRIVER,
                        "Error: Could not find username or passsword input field.")
            return

        send_keys(input_username_login, get_email())
        send_keys(input_password_login, get_password())
        button_login.click()

        self.check_running_wait(2)

        if ("/login" in CHROME_DRIVER.current_url):
            self.complete_captcha()

    def complete_captcha(self):
        self.check_running_wait()

        manual = False

        try:  # FIND AND CLICK ON CAPTCHA CHECKBOX
            captcha_frame = WebDriverWait(CHROME_DRIVER, 3).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
            captcha_checkbox = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                (By.ID, "recaptcha-anchor")))
            captcha_checkbox.click()
        except:
            input(
                "Error: Could not locate CAPTCHA on page. CAPTCHA must be done manually.\nPress enter when done")
            manual = True

        self.check_running_wait(.5)

        # MAKE SURE IT HAS NOT ALREADY FAILED
        if (manual == False):
            try:  # FIND AND CLICK ON THE AUDIO CAPTCHA
                CHROME_DRIVER.switch_to.default_content()
                captcha_frame = WebDriverWait(CHROME_DRIVER, 3).until(
                    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
                captcha_audio_selector = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                    (By.ID, "recaptcha-audio-button")))
                captcha_audio_selector.click()
            except:
                input(
                    "Could not select audio CAPTCHA. CAPTCHA must be done manually.\nPress enter when done")
                manual = True

        self.check_running_wait(.5)

        # MAKE SURE IT HAS NOT ALREADY FAILED
        if (manual == False):
            try:  # CHECK TO SEE IF CAPTCHA HAS FAILED
                captcha_header = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='rc-doscaptcha-header-text']")))
                # CAPTCHA MUST BE DONE MANNUALLY
                CHROME_DRIVER.refresh()
                input(
                    "CAPTCHA has failed. CAPTCHA must be done manually.\nPress enter when done")
                manual = True
            except:  # CAPTCHA DID NOT FAIL
                pass

        try:
            # TODO this will be the CAPTCHA solver
            pass
        except:
            pass

    def get_user_info(self):
        self.check_running_wait()

        try:  # CLICK THE USER DROPDOWN HEADER
            user_profile_dropdown = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dropdown header__account-info__link']")))
            user_profile_dropdown.click()
        except:
            quit_driver(CHROME_DRIVER, "Error: Could not click user dropdown")
            return

        try:  # GO TO THE USERS PROFILE
            user_profile_dropdown_elements = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//a[@class='dropdown__link']")))
            user_profile_dropdown_button = user_profile_dropdown_elements[0]
            user_profile_dropdown_button.click()
        except:
            quit_driver(CHROME_DRIVER,
                        "Error: Could not click user closet button")
            return

        try:  # FIND CURRENTLY FOLLOWED USERS TODO
            following_users = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@data-et-name='following']")))
            set_currently_following(
                self.get_number_format(following_users.text.replace(",", "")))
            print(get_currently_following())
        except:
            quit_driver(CHROME_DRIVER,
                        "Error: Could not obtain currently followed users")
            return

    def search_for_term(self):
        self.check_running_wait()

        # CHECK IF SEARCH TERM IS URL OR NOT
        if ("poshmark.com/user/" in get_searchterm() and "followers" in get_searchterm()):
            try:  # SEARCH FOR INPUT LINK
                redirect(CHROME_DRIVER, get_searchterm())
                follow_user_button = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='al--right btn follow__btn btn--primary m--l--2 m--r--1']")))
            except:  # INPUT LINK WAS NOT A USER PROFILE
                new_term = random.choice(string.ascii_letters)
                print(
                    f"Could not find user profile! Searching by {new_term}")
                redirect(CHROME_DRIVER, LINK +
                         f"search?query={new_term}&type=people")
        else:
            if (".com" in get_searchterm()):  # INPUT LINK WAS NOT A USER PROFILE
                new_term = random.choice(string.ascii_letters)
                print(
                    "Link must be a user's follow page (poshmark.com/user/{username_here}/followers)")
                redirect(CHROME_DRIVER, LINK +
                         f"search?query={new_term}&type=people")
            else:  # INPUT LINK IS JUST A SEARCH TERM
                redirect(CHROME_DRIVER, LINK +
                         f"search?query={get_searchterm()}&type=people")

    def follow_users_recursive(self, counter=1):
        self.check_running_wait()

        try:  # FIND ALL OF THE NAMES & FOLLOW BUTTONS ON THE PAGE
            user_names = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='ellipses fw--med width--100']")))
            follow_buttons = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//button[@data-et-name='follow_user']")))
        except:
            # TODO MAKE IT AUTOMATICALLY EITHER ASK OR SEARCH FOR A DIFFERENT TERM TO START FOLLOWING
            quit_driver(CHROME_DRIVER,
                        "Error: Could not find any follow buttons on page.")
            return

        name_count = 0
        # FOR EACH OF THE FOLLOW BUTTONS, CLICK THEM
        for element in follow_buttons:
            # IF THE TOTAL DESIRED FOLLOW AMOUNT HAS BEEN REACHED
            if (counter == get_desired_follow_amount()):
                quit_driver(f"You have successfully followed {counter} users!")
                break

            # DELAY BETWEEN FOLLOWS & FOLLOW USER
            self.check_running_wait(delay=get_speed())
            self.update_followed(user_names[name_count].text)
            element.click()
            name_count += 1
            counter += 1

        # IF DESIRED AMOUNT OF FOLLOWS WAS NOT REACHED
        if (counter < get_desired_follow_amount()):
            # ATTEMPT TO FIND MORE FOLLOW BUTTONS
            self.follow_users_recursive(counter)

    # COMPLETE POPUP CAPTCHA'S WHILE FOLLOWING
    def complete_popup_captcha(self):
        self.check_running_wait()
        pass

    # UPDATE FOLLOW COUNT
    def update_followed(self, username):
        # ADD USERNAME TO LIST OF NAMES, AND UPDATE TOTAL COUNT
        get_followed().append(username)
        set_follow_count(len(get_followed()))
        try:
            get_window().lcdNumber_followed.display(get_follow_count())
            get_window().listWidget_followed.clear()
            get_window().listWidget_followed.addItems(get_followed())
        except:
            print("Error: Was unable to update GUI. Skipping...")
            return

    # GET STRING IN NUMBER FORMAT
    def get_number_format(self, str):
        num = 0
        try:
            num = (float(re.search(r'\d+\.\d+', str).group()))
        except:
            num = (int(re.search(r'\d+', str).group()))
        return num

    # CALLED TO CHECK IF RUNNING AS WELL AS SLEEP

    def check_running_wait(self, delay=0, str_into="", str_outro=""):
        # if get_running() == False:
        # CHROME_DRIVER.close()
        # get_thread().join()
        #    exit("Process killed.")
        # else:
        if (str_into != ""):
            print(str_into)
        if (delay != 0):
            time.sleep(delay)
        if (str_outro != ""):
            print(str_outro)


Poshmark()
