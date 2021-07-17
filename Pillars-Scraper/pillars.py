import time
from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from driversetup import run_driver
from excel import *


class Page(Enum):
    METRICS = "metrics"
    INCOME_STATEMENT = "income"
    BALANCE_SHEET = "balance"
    CASH_FLOW= "cash"
    PILLARS = "pillars"
    NEWS = "news"
    ANALIZER = "stock_analyzer"

LINK = "https://www.everythingmoney.com/"
CHROME_DRIVER = run_driver()

# LOGIN TO PILLARS
def process_login():
    time.sleep(1)

    # WAS SIGNED OUT FROM PREVIOUS LOGIN
    if ("signed-out" in CHROME_DRIVER.current_url):
        CHROME_DRIVER.get(LINK)

    time.sleep(1)   

    # LOGIN WAS SAVED
    if ("signin" not in CHROME_DRIVER.current_url):
        print("Login has been saved, skipping login.")
        return

    try: # ATTEMPT TO FIND THE USERNAME/PASSWORD INPUTS 
        input_username_login = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        input_password_login = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        button_login = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located((By.XPATH, "//button[@class='mat-focus-indicator mat-button mat-button-base']")))
    except:
        print("Failed to find username, password, or login button.")
        quit()

    # ASK FOR USERNAME AND PASSWORD
    user_input_username = "tehbunk@gmail.com"#input("\nEnter your username\n\t-> ")
    user_input_password = "Bd07252001!"#input("\nEnter your password\n\t-> ")

    try: # SEND USERNAME & PASSWORD 
        input_username_login.clear()
        input_password_login.clear()
        input_username_login.send_keys(user_input_username)
        input_password_login.send_keys(user_input_password)
        button_login.click()
    except:
        print("Failed to login to website. Please try again")
        quit()

    time.sleep(1)

    # CHECK TO SEE IF USERNAME/PASSWORD WAS CORRECT
    if ("signin" in CHROME_DRIVER.current_url):
        print("Login has failed, incorrect username/password?\n")
        process_login()
    
    time.sleep(1)
        
# SEARCH A TICKER SYMBOL
def redirect_to_page(ticker, page):
    time.sleep(1)
    CHROME_DRIVER.get(LINK + f"/company-info/{ticker.upper()}/1/{page.value}") 
    time.sleep(1)

# PULL THE INCOME SHEET DATA 
def get_income():
    time.sleep(1)

    try: # SELECT ANNUAL DATA
        mat_select_combobox = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located((By.XPATH, "//mat-select[@role='combobox']")))     
        mat_select_combobox.click()
        mat_select_options = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//mat-option[@role='option']"))) 
        time.sleep(1)
        for option in mat_select_options:
            if ("Annual" == option.text):
                option.click()
    except:
        print("Failed to select annual data")
        quit()

    income_data = []

    try: # COLLECT INCOME DATA FROM ALL THE CELLS
        income_data_cells = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//td[@role='gridcell']")))    

        count = 0
        cache_data = []
        for cell in income_data_cells:
            if (count % 11 == 0 and count != 0): 
                income_data.append(cache_data)
                cache_data = []
                count = 0 
            if (len(cell.text) < 2 or cell.text == None or cell.text == " "):
                cache_data.append(0.00)
            else: 
                formatted_text = format_cell_text(cell.text, count)
                cache_data.append(formatted_text)
            count += 1
                
    except:
        print("Failed to load income data")
        quit()

    return income_data

def format_cell_text(text, count):
    if (count % 11 == 0): 
        return text
    formatted = text.replace("B", "")
    if ("M" in text):
        fmt_million = text.replace(".", "").replace("M", "")
        if ("$" in fmt_million):
            formatted = fmt_million.replace("$", "$.")
        else:
            formatted = f".{fmt_million}"
    if ("K" in text):
        fmt_thousand = text.replace(".", "").replace("K", "")
        if ("$" in fmt_thousand):
            formatted = fmt_thousand.replace("$", "$.000")
        else:
            formatted = f".000{fmt_thousand}"
    return formatted

# INITILIZE THE PROGRAM
with CHROME_DRIVER:
    CHROME_DRIVER.get(LINK)

    process_login()
    redirect_to_page("intc", Page.INCOME_STATEMENT)
    income_data = get_income()
    
    load_excel()
    create_stock_sheet("intc", income_data, None, None)
    save_excel()
    

    print("done!")

    
    
