
from enum import Enum
from datetime import datetime
from data import *


class Action(Enum):
    BUY = "Purchased"
    SELL = "Sold off"
    DIVIDEND = "Dividend Payout"
    DRIP = "Dividend Reinvested"
    STOCK_SPLIT = "Stock Split"


class AssetType(Enum):
    EQUITY = "Shares"
    CRYPTO = "Coins"
    OPTION = "Contract"


class Asset:
    # Open a new asset position
    def __init__(self, account, ticker, qty, avgcost, assettype, timeline=None):
        self.account = account
        self.ticker = ticker
        self.qty = qty
        self.avgcost = avgcost
        self.assettype = assettype
        self.timeline = timeline

        if (self.timeline is None):
            self.timeline = {self.get_current_date(): Event(
                qty, avgcost, Action.BUY, assettype)}

    # Get last known price of the asset
    def get_price(self):
        return (get_last_price(self.ticker))

    # Get the sector of the asset
    def get_sector(self):
        try:
            return (self.get_info()['sector'])
        except:
            return "Unknown Sector"

    # Get info on stock
    def get_info(self):
        return (get_info(self.ticker))

    # Get current market value of the asset
    def get_market_value(self):
        return (self.qty * self.get_price())

    # Get total cost
    def get_total_cost(self):
        return (self.qty * self.avgcost)

    # Add an event to the timeline
    def add_event(self, qty, price, action):
        self.timeline[self.get_current_date()] = Event(
            qty, price, action, self.assettype)
        self.update_asset(qty, price, action)

    # Update asset after event takes place
    def update_asset(self, qty, price, action):
        total_cost = (self.qty * self.avgcost)
        event_cost = (qty * price)
        # Simply buying asset        # DRIP treated same as buy
        if (action is Action.BUY or action is Action.DRIP):
            self.qty += qty
            self.avgcost = (total_cost + event_cost) / self.qty
        # Simply selling asset
        if (action is Action.SELL):
            self.qty -= qty
            self.avgcost = (total_cost - event_cost) / self.qty
        # For dividend qty will be the yield, price will be the money received
        if (action is Action.DIVIDEND):
            pass
        # Stock split ratio will be counted at 'qty/price' ex 5/1 or 1/5
        if (action is Action.STOCK_SPLIT):
            if (qty == 1):
                self.qty = (self.qty * price)
                self.avgcost = (self.avgcost / price)
            else:
                self.qty = (self.qty / qty)
                self.avgcost = (self.avgcost * qty)

    def get_current_date(self):
        return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


class Event:
    # Create a new event for an assets timeline
    def __init__(self, qty, price, action, assettype):
        self.qty = qty
        self.price = price
        self.action = action
        self.desc = (f"{action.value} {qty} {assettype.value} at ${price}" if (  # Todo this will need changing
            action != Action.DIVIDEND) and (action != Action.STOCK_SPLIT) else f"{action.value}")
