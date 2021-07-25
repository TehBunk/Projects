import os
import json
import pandas as pd
from backend import *
from pathlib import Path
from datetime import datetime

from pkg_resources import get_distribution


class Company:
    def __init__(self, ticker, date=None, data=None, save=False):
        self.ticker = ticker.upper()
        self.date = (self.get_string_date(datetime.now())
                     if date == None else date)
        self.data = data
        if (save):
            self.save_company_data()

    def get_data(self):
        return self.data

    def get_directory(self):
        dir = os.getcwd() + f"/Pillars-Scraper/comp_data/{self.ticker}/"
        Path(dir).mkdir(parents=True, exist_ok=True)
        return dir

    def save_company_data(self):
        print(f"Saving {self.ticker} data...")
        dir = self.get_directory()
        file = open(f"{dir}data.txt", 'w')

        data = {"Ticker": self.ticker, "Date": self.date}
        json.dump(data, file)

        if (self.data is not None):
            self.data.to_csv(r"{0}data.csv".format(dir))
        # if (self.balancedata is not None):
        #     self.balancedata.to_csv(r"{0}balance.csv".format(dir))
        # if (self.cashflowdata is not None):
        #     self.cashflowdata.to_csv(r"{0}cashflow.csv".format(dir))

    def get_string_date(self, date):
        return date.strftime("%m-%d-%Y")


def load_companys():
    companies = []

    dir = os.getcwd() + "/Pillars-Scraper/comp_data/"
    dirs = os.listdir(dir)
    if (os.path.isdir(dir) == False or len(dirs) == 0):
        print("No companies to load, skipping.")
        return

    for name in dirs:
        try:
            cdir = f"{dir}{name}/"
            file = open(f"{cdir}data.txt")

            data = json.load(file)
            ticker = data["Ticker"]
            date = data["Date"]

            df_data = pd.read_csv(f"{cdir}data.csv", index_col=0)

            companies.append(Company(ticker, date, df_data))
            print(f"Company data has been loaded for - {ticker}")
        except:
            print(f"Failed to load files for {cdir}")

    print(f"\nLoaded {len(companies)} companies...\n")
    return companies
