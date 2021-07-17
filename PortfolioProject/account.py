# Use pickle to save portfolil

import uuid
from assets import Asset


class Account:
    # Create new account
    def __init__(self, name, assets=None, id=uuid.uuid1()):
        self.id = id
        self.name = name
        self.assets = assets

        # Assets will be stored by their ticker symbol
        if (assets == None):
            self.assets = {}

    # Get asset
    def get_asset(self, ticker):
        return self.assets[ticker]

    # Add a new asset (open a position)
    def add_asset(self, ticker, qty, price, assettype):
        self.assets[ticker] = Asset(self.id, ticker, qty, price, assettype)

    # Get the current market value of the whole account
    def get_market_value(self):
        total = 0
        for asset in self.assets.values():
            total += asset.get_market_value()
        return total

    # Get total cost of the whole account
    def get_total_cost(self):
        total = 0
        for asset in self.assets.values():
            total += asset.get_total_cost()
        return total
