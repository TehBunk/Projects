import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import urllib.request
import undetected_chromedriver.v2 as uc

driver = None


def open_chrome():
    global driver

    options = uc.ChromeOptions()

    # setting profile
    options.user_data_dir = "c:\\temp\\profile"

    # another way to set profile is the below (which takes precedence if both variants are used
    options.add_argument('--user-data-dir=c:\\temp\\profile2')

    # just some options passing in to skip annoying popups
    options.add_argument(
        '--no-first-run --no-service-autorun --password-store=basic')
    driver = uc.Chrome(options=options)


open_chrome()

# PATH = "C:\\Users\\camer\\Desktop\\Poshmark\\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
test_email = "spuffygaming@gmail.com"
test_password = "Bumblebee098!!"
text_to_speech = "https://speech-to-text-demo.ng.bluemix.net/"
other_page = 0
login = 0


def do_captcha():
    global other_page
    global login
    global pattern
    global new_string
    try:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
            time.sleep(1)
            driver.switch_to.default_content()
            time.sleep(1)
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".rc-audiochallenge-play-button button")))
            time.sleep(2)
        except:
            # get the mp3 audio file
            src = driver.find_element_by_id(
                "audio-source").get_attribute("src")
            print("Url:", src)
            urllib.request.urlretrieve(src, "src.mp3")
            time.sleep(2)
            # 0 = Posh # 1 = Text to speech
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            root = driver.find_element_by_id('root').find_elements_by_class_name(
                'dropzone _container _container_large')
            btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
            btn.send_keys('C:/Users/camer/Desktop/Poshmark/src.mp3')
            # Audio to text is processing
            time.sleep(10)
            # btn.send_keys(path)
            print("4")
            # Audio to text is processing
            time.sleep(10)
            print("5")
            text = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div/div[7]/div/div/div').find_elements_by_tag_name('span')
            print("5.1")
            result = " ".join([each.text for each in text])
            print("6")
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            print("7")
            remove_period = "."
            pattern = "[" + remove_period + "]"
            new_string = re.sub(pattern, "", result)
            new_string = string.capwords(new_string)
            print(new_string)
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'audio-response'))).send_keys(
                new_string, Keys.ENTER)
            time.sleep(5)
            driver.switch_to.default_content()
    except:
        if login == 1:
            time.sleep(3)
            driver.switch_to.default_content()
            input(
                "Captcha Bypass Has Failed, Please Press The '""Login Button""' And Manually Do Captcha, And Then Press Enter In Console...")
            login == 0
        if other_page == 1:
            pass


try:
    actions = ActionChains(driver)
    account_email = test_email
    account_password = test_password
    driver.get("https://poshmark.com/")
    time.sleep(3)
    driver.execute_script("window.open('{}');".format(text_to_speech))
    time.sleep(3)
    # 0 = Posh # 1 = Text to speech
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav/div/div/a[1]")
    login_button.click()
    time.sleep(3)
    email_path = driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[1]/input")
    password_path = driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[2]/input")
    email_path.send_keys(account_email)
    password_path.send_keys(account_password)
    sign_in_button = driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[3]/button")
    sign_in_button.click()
    time.sleep(3)
    drop_down_listings = driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav[1]/div/div/form/div[1]/div[1]/div/div[1]/span")
except NoSuchElementException:
    try:
        login = 1
        do_captcha()
        time.sleep(3)
        driver.switch_to.default_content()
        captcha_login = driver.find_element_by_xpath(
            "/html/body/div[1]/main/div[2]/div/div/div/div[3]/form/div[5]/button")
        captcha_login.click()
    except NoSuchElementException:
        pass
time.sleep(3)
find_my_profile_button = None
find_how_many_followers = None
followers_to_remove = None
pattern = None
how_many_followers = None
new_string = None
how_many_int_first = None


def find_users():
    global find_my_profile_button
    global find_how_many_followers
    global followers_to_remove
    global pattern
    global new_string
    global how_many_int_first
    global how_many_followers

    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
    find_my_profile_button = driver.find_element_by_xpath(
        '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')
    find_my_profile_button.click()
    time.sleep(3)
    find_how_many_followers = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/div[2]/div/div[2]/nav/ul/li[4]/div')
    how_many_followers = find_how_many_followers.text
    followers_to_remove = "\nFollowing,"
    pattern = "[" + followers_to_remove + "]"
    new_string = re.sub(pattern, "", how_many_followers)
    how_many_int_first = int(new_string)
    print("Currently following: ", how_many_int_first, " Users.")
    find_posh_logo = driver.find_element_by_xpath(
        '//*[@id="app"]/header/nav[1]/div/a/img')
    find_posh_logo.click()
    time.sleep(7)


find_users()

try:
    find_notifications_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[2]/button[1]')
    find_notifications_button.click()
except:
    pass
try:
    drop_down_listings = driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav[1]/div/div/form/div[1]/div[1]/div/div[1]/span")

    drop_down_listings.click()
    drop_down_people = driver.find_element_by_xpath(
        "/html/body/div[1]/header/nav[1]/div/div/form/div[2]/span[2]")
    drop_down_people.click()

except:
    pass

time.sleep(2)
search_bar = driver.find_element_by_xpath(
    "/html/body/div[1]/header/nav[1]/div/div/form/div[1]/div[2]/div[1]/div/input")
search = input(" What do want to follow? "
               "\n If you have a term you want to search, search it. "
               "\n If you wanna follow a page, link it. "
               "\n If you are already on the page, just press Enter: ")
if ".com" in search:
    driver.get(search)
else:
    if not search:
        pass
    else:
        search_bar.send_keys(search)
        search_bar.send_keys(Keys.RETURN)
time.sleep(3)
follow_amount = 1
amount_to_follow = input("How many people do you want to follow?: ")
amount_to_follow = int(amount_to_follow) + 1
speed = input("Please input follow speed (Recommended to use .8): ")
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
            if driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/h5'):
                try:
                    other_page = 1
                    do_captcha()
                except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
                    try:
                        driver.switch_to.default_content()
                        time.sleep(3)
                        driver.switch_to.default_content()
                        find_close_button = driver.find_element_by_xpath(
                            '/html/body/div[1]/div/div/div[2]/div[1]/button/i')
                        find_close_button.click()
                    except(TimeoutException, ElementClickInterceptedException, NoSuchElementException):
                        input(
                            "Bypass has failed, please manually follow a User, do the captcha, then press enter.")
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            try:
                if driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]'):
                    time.sleep(3)
                    driver.switch_to.default_content()
                    # input("Bypass has failed, please manually follow a User, do the captcha, then press enter.")
            except NoSuchElementException:
                pass
            pass

        amount_to_string = str(follow_amount)
        find_follow_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button')
        try:
            not_following = driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[3]/div/div[' + amount_to_string + ']/button')
            not_following_text = not_following.text
            not_following_string = str(not_following_text)
        except:
            not_following_string = " "
            try:
                not_following_2 = driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button')
                not_following_text_2 = not_following_2.text
                not_following_string_2 = str(not_following_text_2)
            except:
                pass

        find_user_name = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/a/div/div')
        found_username = find_user_name.text
        follow_user = 0

        if "Following" in not_following_string:
            print("Already Following: ", found_username)
            already_followed += 1
            follow_user = 1
            follow_amount += 1

        if "Following" in not_following_string_2:
            print("Already Following: ", found_username)
            already_followed += 1
            follow_user = 1
            follow_amount += 1

        if "Follow" in not_following_string and follow_user == 0:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
            print("Clicked: ", str(real_follow + 1),
                  "Their Username is: ", found_username)
            follow_amount += 1

        if "Follow" in not_following_string_2 and follow_user == 0:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
            print("Clicked: ", str(real_follow + 1),
                  "Their Username is: ", found_username)
            follow_amount += 1

        follow_user = 0
        # print("Program has followed: ", amount_to_string)
        # print("You have already followed: ", already_followed)
        # print("How Many Users You Actually Followed:", real_follow)
        driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
        # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))))
        time.sleep(speed_float)

        final_follow = int(amount_to_string)
        real_follow = (final_follow - already_followed)
        if real_follow == (amount_to_follow - 1):
            driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
            find_my_profile_button = driver.find_element_by_xpath(
                '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')
            find_my_profile_button.click()
            time.sleep(3)
            find_how_many_followers = driver.find_element_by_xpath(
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
            driver.close()
            exit("Program finished.")
    except (ElementNotInteractableException, TimeoutException, NoSuchElementException):
        try:
            print("Threw an exception... Trying To Continue To Load Page")
            follow_amount += 1
            try:
                driver.switch_to.default_content()
                time.sleep(3)
                driver.switch_to.default_content()
                find_close_button = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[1]/button/i')
                find_close_button.click()
                print(
                    "The Exception that was thrown is that the captcha prompt was not closed.. Should be closed now =)")
            except(TimeoutException, ElementClickInterceptedException, NoSuchElementException):
                pass
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="content"]/div/div/div/div[' + amount_to_string + ']/button'))))
            time.sleep(3)
            pass
        except (ElementNotInteractableException, TimeoutException, NoSuchElementException):
            driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[1]/div'))))
            find_my_profile_button = driver.find_element_by_xpath(
                '//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')
            find_my_profile_button.click()
            time.sleep(3)
            find_how_many_followers = driver.find_element_by_xpath(
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
            driver.close()
            exit("Program finished.")
