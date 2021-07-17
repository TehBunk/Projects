from data import get_ticker
from data import get_info
import pickle
from assets import Action, AssetType
from portfolio import Porftolio

# port = Porftolio("Porfolio Test")
# port.add_account("Account 1")
# port.add_account("Account 2")

# account = port.get_account("Account 1")
# account.add_asset("MSFT", 10, 100, AssetType.EQUITY)
# account.add_asset("IBM", 10, 150, AssetType.CRYPTO)
# account.add_asset("AAPL", 10, 200, AssetType.OPTION)
# port.get_account("Account 2").add_asset("TSLA", 10, 50, AssetType.EQUITY)

# msft = account.get_asset("MSFT")
# msft.add_event(10, 200, Action.BUY)
# msft.add_event(10, 220, Action.SELL)

# print(port.id)
# print(port.accounts.keys())

# for account in port.accounts.values():
#     print(account.assets.keys())

# info = msft.get_info()

# for key in info.keys():
#     print(f"{key} - {info[key]}\n")



#print("\n\n---------------\n\n")

#dbfile = open('examplePickle', 'ab')  
#pickle.dump(port, dbfile)
#dbfile.close()

#dbfile = open('examplePickle', 'rb')  
#db = pickle.load(dbfile)
#dbfile.close()


#print(port.id)
#print(port.accounts.keys())

#for account in port.accounts.values():
#    print(account.assets.keys())



