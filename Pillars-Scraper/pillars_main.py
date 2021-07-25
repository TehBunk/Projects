
import time
import traceback
import numpy as np
import pandas as pd
from enum import Enum
from backend import drop_dupes
from pcompany import *


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from driversetup import run_driver


class Page(Enum):
    METRICS = "metrics"
    INCOME_STATEMENT = "income"
    BALANCE_SHEET = "balance"
    CASH_FLOW = "cash"
    PILLARS = "pillars"
    NEWS = "news"
    ANALIZER = "stock_analyzer"


LINK = "https://www.everythingmoney.com/"
CHROME_DRIVER = None

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

    try:  # ATTEMPT TO FIND THE USERNAME/PASSWORD INPUTS
        input_username_login = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        input_password_login = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        button_login = WebDriverWait(CHROME_DRIVER, 3).until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='mat-focus-indicator mat-button mat-button-base']")))
    except:
        print("Failed to find username, password, or login button.")
        quit()

    # ASK FOR USERNAME AND PASSWORD
    # input("\nEnter your username\n\t-> ")
    user_input_username = "tehbunk@gmail.com"
    # input("\nEnter your password\n\t-> ")
    user_input_password = "Bd07252001!"

    try:  # SEND USERNAME & PASSWORD
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


# used to get the income data from current page
def scrape_page(blocks):
    time.sleep(1)

    try:  # select annual data combo box
        mat_select_combobox = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@role='combobox']")))
        mat_select_combobox.click()
        mat_select_options = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_all_elements_located((By.XPATH, "//mat-option[@role='option']")))
        time.sleep(1)
        for option in mat_select_options:
            if (option.text == "Annual"):
                option.click()
    except:
        print("Failed to select annual data type, trying again.")
        return scrape_page(blocks)

    return get_page_data(blocks)


def get_page_data(blocks):
    data_frame = None
    temp_data = []

    try:  # load data from the current page
        header_data_cells = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_all_elements_located((By.XPATH, "//th[@role='columnheader']")))
        income_data_cells = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_all_elements_located((By.XPATH, "//td[@role='gridcell']")))

        dates_arr = []
        total_cols = int((len(header_data_cells) / blocks))
        # these are the dates listed
        for pos in range(0, (total_cols - 1)):
            dates_arr.append(
                (header_data_cells[pos + 1].text).replace("-12", ""))

        # count = 0
        # fix_last = 0
        # cache_data = []
        # # for each and every cell on the page (not including headers)
        # for cell in income_data_cells:
        #     # at the end of the row
        #     if (count % total_cols == 0 and count != 0):
        #         temp_data.append(cache_data)
        #         cache_data = []
        #         count = 0
        #     # if the row is blank and has no value
        #     if len(cell.text) < 2 or cell.text is None or cell.text == " ":
        #         cache_data.append("N/A")
        #     else:  # format the value to be in billions
        #         formatted_text = format_cell_text(cell.text, count)
        #         cache_data.append(formatted_text)
        #     count += 1

        cache_data = []
        # loop thru from 0-352
        for cell_number in range(0, len(income_data_cells)):
            # at the end of the row
            cell = income_data_cells[cell_number]
            if ((cell_number % (total_cols) == 0 and cell_number != 0) or cell_number == len(income_data_cells) - 1):
                temp_data.append(format_arr(cache_data))
                print(cache_data)
                cache_data = []
            # if the row is blank and has no value
            if len(cell.text) < 2 or cell.text is None or cell.text == " ":
                cache_data.append(np.nan)
            else:  # format the value to be in billions
                cache_data.append(cell.text)

        data_dic = {}
        # for each of the rows in the table
        for row in temp_data:
            pos = 0
            title = None
            cache_arr = []
            # get each of the cells in that row
            for cell in row:
                # if it is the first cell in the row its the title
                if (pos == 0):
                    title = cell
                else:  # otherwise its just anotha value
                    cache_arr.append(cell)
                pos += 1
            data_dic[title] = cache_arr

        data_frame = pd.DataFrame.from_dict(
            data_dic, columns=dates_arr, orient='index')

    except:  # failed to load data some reason...
        print("Failed while loading income data.")
        traceback.print_exc()
        CHROME_DRIVER.quit()
        quit()

    try:  # check for next page (if this doesn't except there was a new page)
        print("Searching for next page...")
        next_page_icon = WebDriverWait(CHROME_DRIVER, 3).until(
            EC.presence_of_element_located((By.XPATH, "//mat-icon[.='chevron_right']")))
        next_page_icon.click()
        # concat dataframe from next page (recrusive loop)
        return pd.concat([data_frame, get_page_data(blocks)], axis=1, ignore_index=False)
    except:  # there was no next page, break recusion, return dataframe
        print("No more pages found.")
        return data_frame


def format_arr(arr):
    for i in range(1, len(arr)):
        arr[i] = format_str(arr[i])
    return arr


def format_str(str):
    if (type(str) is float):
        return str

    formatted = str.replace("B", "")

    if ("M" in formatted):
        formatted = formatted.replace(".", "").replace("M", "")
        if ("$" in formatted):
            formatted = formatted.replace("$", "0.")
        elif ("-" in formatted):
            formatted = formatted.replace("-", "-0.")
        else:
            formatted = f".{formatted}"
    if ("K" in formatted):
        formatted = formatted.replace(".", "").replace("K", "")
        if ("$" in formatted):
            formatted = formatted.replace("$", "0.000")
        elif ("-" in formatted):
            formatted = formatted.replace("-", "-0.000")
        else:
            formatted = f".000{formatted}"
    return formatted.replace("$", "")


def scrape_company(ticker, save=True):
    print(f"Attempting to scrape data for {ticker.upper()}.")
    global CHROME_DRIVER

    CHROME_DRIVER = run_driver()
    CHROME_DRIVER.get(LINK)
    process_login()

    redirect_to_page(ticker, Page.INCOME_STATEMENT)
    income_data = scrape_page(4)
    redirect_to_page(ticker, Page.BALANCE_SHEET)
    balance_data = scrape_page(3)
    redirect_to_page(ticker, Page.CASH_FLOW)
    cashflow_data = scrape_page(5)

    print(f"{ticker.upper()} Data has been scraped.")
    if (CHROME_DRIVER != None):
        CHROME_DRIVER.quit()

    id = drop_dupes(income_data)
    bd = drop_dupes(balance_data)
    cd = drop_dupes(cashflow_data)
    data = pd.concat([id, bd, cd]).drop_duplicates()
    return Company(ticker, None, data, save)
