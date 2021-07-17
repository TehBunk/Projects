from enum import Enum
import yfinance as yf


# Get the ticker data
def get_ticker(ticker):
    return yf.Ticker(ticker)


# Get the last price of the ticker
def get_last_price(ticker):  # Switch to live price at some point
    return get_history(ticker, TimePeriod.ONE_DAY, HistoryType.CLOSE)[0]


# Get stock history
def get_history(ticker, time_period, history_type):
    data = get_ticker(ticker)
    price_data = data.history(period=time_period.value)
    return price_data[history_type.value]

def get_info(ticker):
    return get_ticker(ticker).info

class HistoryType(Enum):
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
    DIVIDEND = "Dividends"
    STOCK_SPLIT = "Stock Splits"


class TimePeriod(Enum):
    ONE_DAY = "1d"
    FIVE_DAY = "5d"
    ONE_MONTH = "1mo"
    THREE_MONTH = "3mo"
    SIX_MONTH = "6mo"
    ONE_YEAR = "1y"
    TWO_YEAR = "2y"
    FIVE_YEAR = "5y"
    TEN_YEAR = "10y"
    YEAR_TO_DATE = "ytd"
    MAX = "max"
