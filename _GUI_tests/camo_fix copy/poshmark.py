
from tempfile import tempdir
from vardata import *
import string
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import sys
import urllib.request
import undetected_chromedriver.v2 as uc

DRIVER = None

text_to_speech = "https://speech-to-text-demo.ng.bluemix.net/"
other_page = 0
login = 0
find_my_profile_button = None
find_how_many_followers = None
followers_to_remove = None
pattern = None
how_many_followers = None
new_string = None
how_many_int_first = None


def run_driver():
    global DRIVER

    options = uc.ChromeOptions()

    # setting profile
    options.user_data_dir = "c:\\temp\\profile"

    # another way to set profile is the below (which takes precedence if both variants are used
    options.add_argument('--user-data-dir=c:\\temp\\profile2')

    # just some options passing in to skip annoying popups
    options.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    DRIVER = uc.Chrome(options=options)
    # PATH = "C:\\Users\\camer\\Desktop\\Poshmark\\chromedriver.exe"
    # driver = webdriver.Chrome(PATH)


def do_captcha():
    global other_page
    global login
    global pattern
    global new_string
    try:
        try:
            WebDriverWait(DRIVER, 20).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
            WebDriverWait(DRIVER, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()

            check_running_wait(1)
            DRIVER.switch_to.default_content()
            check_running_wait(1)

            WebDriverWait(DRIVER, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
            WebDriverWait(DRIVER, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
            check_running_wait(2)
            WebDriverWait(DRIVER, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".rc-audiochallenge-play-button button")))

            check_running_wait(2)
        except:
            # get the mp3 audio file
            src = DRIVER.find_element_by_id(
                "audio-source").get_attribute("src")
            print("Url:", src)

            urllib.request.urlretrieve(src, os.getcwd() + "/src.mp3")
            check_running_wait(2)
            # 0 = Posh # 1 = Text to speech
            DRIVER.switch_to.window(DRIVER.window_handles[1])
            check_running_wait(2)
            root = DRIVER.find_element_by_id('root').find_elements_by_class_name(
                'dropzone _container _container_large')

            btn = DRIVER.find_element(By.XPATH, '//*[@id="root"]/div/input')
            btn.send_keys(os.getcwd() + '/src.mp3')
            # Audio to text is processing
            check_running_wait(10)
            # btn.send_keys(path)

            # Audio to text is processing
            check_running_wait(10)

            text = DRIVER.find_element(By.XPATH,
                                       '//*[@id="root"]/div/div[7]/div/div/div').find_elements_by_tag_name('span')

            result = " ".join([each.text for each in text])
            DRIVER.switch_to.window(DRIVER.window_handles[0])
            check_running_wait(3)

            remove_period = "."
            pattern = "[" + remove_period + "]"
            new_string = re.sub(pattern, "", result)
            new_string = string.capwords(new_string)

            print(new_string)
            check_running_wait(3)
            WebDriverWait(DRIVER, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
            WebDriverWait(DRIVER, 20).until(EC.element_to_be_clickable((By.ID, 'audio-response'))).send_keys(
                new_string, Keys.ENTER)

            check_running_wait(5)
            DRIVER.switch_to.default_content()
    except:
        print("Error 88")
        if login == 1:
            check_running_wait(3)
            DRIVER.switch_to.default_content()
            #input("Captcha Bypass Has Failed, Please Press The '""Login Button""' And Manually Do Captcha, And Then Press Enter In Console...")

            login == 0
        if other_page == 1:
            pass


def login_site():
    try:
        actions = ActionChains(DRIVER)
        DRIVER.get("https://poshmark.com/")

        check_running_wait(3)
        DRIVER.execute_script("window.open('{}');".format(text_to_speech))
        check_running_wait(3)
        # 0 = Posh # 1 = Text to speech
        DRIVER.switch_to.window(DRIVER.window_handles[0])
        check_running_wait(2)

        login_button = DRIVER.find_element_by_xpath(
            "/html/body/div[1]/header/nav/div/div/a[1]")
        login_button.click()

        check_running_wait(3)

        email_path = DRIVER.find_element_by_xpath(
            "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[1]/input")
        password_path = DRIVER.find_element_by_xpath(
            "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[2]/input")
        sign_in_button = DRIVER.find_element_by_xpath(
            "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[3]/button")

        email_path.send_keys(Keys.CONTROL, 'a')
        email_path.send_keys(Keys.DELETE)
        password_path.send_keys(Keys.CONTROL, 'a')
        password_path.send_keys(Keys.DELETE)
        email_path.send_keys(get_email())  # Email
        password_path.send_keys(get_password())  # Password

        sign_in_button.click()

        check_running_wait(3)
        drop_down_listings = DRIVER.find_element_by_xpath(
            "/html/body/div[1]/header/nav[1]/div/div/form/div[1]/div[1]/div/div[1]/span")
    except NoSuchElementException:
        print("Error 69")
        try:
            login = 1
            do_captcha()
            check_running_wait(3)
            DRIVER.switch_to.default_content()
            captcha_login = DRIVER.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[5]/button")
            captcha_login.click()
        except NoSuchElementException:
            print("Error 99")
    check_running_wait(3)


def find_users():
    global find_my_profile_button
    global find_how_many_followers
    global followers_to_remove
    global pattern
    global new_string
    global how_many_int_first
    global how_many_followers

    DRIVER.execute_script("arguments[0].click();", WebDriverWait(DRIVER, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
    find_my_profile_button = DRIVER.find_element_by_xpath(
        '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')
    find_my_profile_button.click()
    check_running_wait(3)
    find_how_many_followers = DRIVER.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/div[2]/div/div[2]/nav/ul/li[4]/div')
    how_many_followers = find_how_many_followers.text
    followers_to_remove = "\nFollowing,"

    pattern = "[" + followers_to_remove + "]"
    new_string = re.sub(pattern, "", how_many_followers)
    how_many_int_first = int(new_string)

    print("Currently following: ", how_many_int_first, " Users.")
    find_posh_logo = DRIVER.find_element_by_xpath(
        '//*[@id="app"]/header/nav[1]/div/a/img')
    find_posh_logo.click()
    check_running_wait(7)


def main_code(search_term, speed, amount_to_follow):
    # IF ZERO IS PASSED IN, SET TO INFINITY
    if (amount_to_follow == "0"):
        amount_to_follow = str(sys.maxsize)
    # CHECK IF LINK
    if (".com" in search_term):
        print("test")
        DRIVER.get(search_term)
    else:
        try:
            find_notifications_button = DRIVER.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/button[1]')
            find_notifications_button.click()
        except:
            print("Error 1")

        try:
            drop_down_listings = DRIVER.find_element_by_xpath(
                "/html/body/div[1]/header/nav[1]/div/div/form/div[1]/div[1]/div/div[1]/span")

            drop_down_listings.click()
            drop_down_people = DRIVER.find_element_by_xpath(
                "/html/body/div[1]/header/nav[1]/div/div/form/div[2]/span[2]")
            drop_down_people.click()
        except:
            print("Error 2")

        check_running_wait(2)

        search_bar = DRIVER.find_element_by_xpath(
            "/html/body/div[1]/header/nav[1]/div/div/form/div[1]/div[2]/div[1]/div/input")

        search_bar.send_keys(search_term)  # input("Search What?: ")
        search_bar.send_keys(Keys.RETURN)

    check_running_wait(3)

    followed_amount = 1
    # input("How many people do you want to follow?: ")
    amount_to_follow = int(amount_to_follow) + 1

    #speed = input("Please input follow speed (Recommended to use .8): ")
    speed_float = float(speed)
    not_following_string = " "
    not_following_string_2 = " "
    already_followed = 0
    final_follow = 0
    real_follow = 0

    while real_follow != amount_to_follow:
        try:
            # if follow_amount == amount_to_follow:
            #   exit("Followed All " + amount_to_string + " Accounts.")
            try:
                if DRIVER.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/h5'):
                    try:
                        other_page = 1
                        do_captcha()
                    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
                        print("Error 3")
                        try:
                            DRIVER.switch_to.default_content()
                            check_running_wait(3)
                            DRIVER.switch_to.default_content()
                            find_close_button = DRIVER.find_element_by_xpath(
                                '/html/body/div[1]/div/div/div[2]/div[1]/button/i')
                            find_close_button.click()
                        except(TimeoutException, ElementClickInterceptedException, NoSuchElementException):
                            print("Error 4")
                            # TODO input("Bypass has failed, please manually follow a User, do the captcha, then press enter.")
            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
                print("Error 5")
                try:
                    if DRIVER.find_element_by_xpath('/html/body/div/div/div[1]/div[1]'):
                        check_running_wait(3)
                        DRIVER.switch_to.default_content()
                        # input("Bypass has failed, please manually follow a User, do the captcha, then press enter.")
                except NoSuchElementException:
                    print("Error 6")
                    pass
                pass

            try:
                amount_to_string = str(followed_amount)
                find_follow_button = DRIVER.find_element_by_xpath(
                    '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button')
                not_following = DRIVER.find_element_by_xpath(
                    '//*[@id="content"]/div/div[3]/div/div[' + amount_to_string + ']/button')
                not_following_text = not_following.text
                not_following_string = str(not_following_text)
            except:
                print("Error 7")
                not_following_string = " "
                try:
                    not_following_2 = DRIVER.find_element_by_xpath(
                        '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button')
                    not_following_text_2 = not_following_2.text
                    not_following_string_2 = str(not_following_text_2)
                except:
                    print("Error 8")
                    pass
            try:
                find_user_name = DRIVER.find_element_by_xpath(
                    '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/a/div/div')
                found_username = find_user_name.text
                follow_user = 0

                print('debug')

                if "Following" in not_following_string:
                    print("Already Following: ", found_username)
                    already_followed += 1
                    follow_user = 1
                    followed_amount += 1

                print('debug1')

                if "Following" in not_following_string_2:
                    print("Already Following: ", found_username)
                    already_followed += 1
                    follow_user = 1
                    followed_amount += 1

                print('debug2')

                if "Follow" in not_following_string and follow_user == 0:
                    DRIVER.execute_script("arguments[0].click();",
                                          WebDriverWait(DRIVER, 20).until(EC.element_to_be_clickable(
                                              (By.XPATH,
                                               '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
                    print("Clicked: ", str(real_follow + 1),
                          "Their Username is: ", found_username)
                    get_followed().append(found_username)
                    update_followed()
                    followed_amount += 1

                print('debug3')

                if "Follow" in not_following_string_2 and follow_user == 0:
                    DRIVER.execute_script("arguments[0].click();",
                                          WebDriverWait(DRIVER, 20).until(EC.element_to_be_clickable(
                                              (By.XPATH,
                                               '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
                    print("Clicked: ", str(real_follow + 1),
                          "Their Username is: ", found_username)
                    get_followed().append(found_username)
                    update_followed()
                    followed_amount += 1
            except:
                print(f"Error 9 {amount_to_string}")

            try:
                follow_user = 0
                # print("Program has followed: ", amount_to_string)
                # print("You have already followed: ", already_followed)
                # print("How Many Users You Actually Followed:", real_follow)
                DRIVER.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(DRIVER, 30).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
                # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))))
                check_running_wait(speed_float)

                final_follow = int(amount_to_string)
                real_follow = (final_follow - already_followed)

                if real_follow == (amount_to_follow - 1):
                    DRIVER.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(DRIVER, 20).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
                    DRIVER.execute_script("arguments[0].click();", WebDriverWait(DRIVER, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
                    find_my_profile_button = DRIVER.find_element_by_xpath(
                        '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')
                    find_my_profile_button.click()
                    check_running_wait(3)
                    find_how_many_followers = DRIVER.find_element_by_xpath(
                        '//*[@id="content"]/div/div[1]/div/div[2]/div/div[2]/nav/ul/li[4]/div')
                    how_many_followers = find_how_many_followers.text
                    followers_to_remove = "\nFollowing,"

                    pattern = "[" + followers_to_remove + "]"
                    new_string = re.sub(pattern, "", how_many_followers)
                    how_many_int_second = int(new_string)
                    how_many_followed = how_many_int_second - how_many_int_first

                    print("Followed All " + str((final_follow - already_followed)) + " Accounts. ",
                          "The program only followed: ",
                          str(how_many_followed),
                          " Users.")

                    DRIVER.close()
                    exit("Program finished.")
            except:
                print("Error 10")
        except (ElementNotInteractableException, TimeoutException, NoSuchElementException):
            print("Error 11")
            try:
                print("Threw an exception... Trying To Continue To Load Page")
                followed_amount += 1
                try:
                    DRIVER.switch_to.default_content()
                    check_running_wait(3)
                    DRIVER.switch_to.default_content()
                    find_close_button = DRIVER.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[2]/div[1]/button/i')
                    find_close_button.click()
                    print(
                        "The Exception that was thrown is that the captcha prompt was not closed.. Should be closed now =)")
                except(TimeoutException, ElementClickInterceptedException, NoSuchElementException):
                    print("Error 12")
                    pass

                DRIVER.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                DRIVER.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(DRIVER, 30).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
                check_running_wait(3)
                pass
            except (ElementNotInteractableException, TimeoutException, NoSuchElementException):
                print("Error 13")
                DRIVER.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(DRIVER, 20).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
                DRIVER.execute_script("arguments[0].click();", WebDriverWait(DRIVER, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))

                find_my_profile_button = DRIVER.find_element_by_xpath(
                    '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')
                find_my_profile_button.click()

                check_running_wait(3)
                find_how_many_followers = DRIVER.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/div[2]/div/div[2]/nav/ul/li[4]/div')
                how_many_followers = find_how_many_followers.text

                followers_to_remove = "\nFollowing,"
                pattern = "[" + followers_to_remove + "]"
                new_string = re.sub(pattern, "", how_many_followers)

                how_many_int_second = int(new_string)
                how_many_followed = how_many_int_second - how_many_int_first

                print("Followed All " + str((final_follow - already_followed)) + " Accounts. ",
                      "The program only followed: ",
                      str(how_many_followed),
                      " Users.")

                DRIVER.close()
                exit("Program finished.")


def check_running_wait(delay):
    if get_running() == False:
        DRIVER.close()
        # get_thread().join()
        exit("Process killed.")
    else:
        time.sleep(delay)

# UPDATE THE FOLLOWED LIST AND COUNTER


def update_followed():
    set_follow_count(len(get_followed()))
    get_window().lcdNumber_followed.display(get_follow_count())
    get_window().listWidget_followed.clear()
    get_window().listWidget_followed.addItems(get_followed())
