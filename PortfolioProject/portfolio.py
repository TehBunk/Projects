# Use pickle to save portfolil

import uuid
from account import Account
from assets import Asset


class Porftolio:
    # Create new Porftolio
    def __init__(self, name, accounts=None, id=uuid.uuid1()):
        self.id = id
        self.name = name
        self.accounts = accounts

        # Accounts will be stored by their name
        if (accounts == None):
            self.accounts = {}

    # Get account
    def get_account(self, name):
        return self.accounts[name]

    # Add a new asset (open a position)
    def add_account(self, name):
        self.accounts[name] = Account(name)

    # Get the current market value of the whole portfolio
    def get_market_value(self):
        total = 0
        for account in self.accounts.values():
            total += account.get_market_value()
        return total

    # Get total cost of the whole portfolio
    def get_total_cost(self):
        total = 0
        for account in self.accounts.values():
            total += account.get_total_cost()
        return total
