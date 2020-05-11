import requests
import json

r_deribit = requests.get("https://test.deribit.com/api/v2/public/get_order_book?depth=5&instrument_name=BTC-PERPETUAL")
print(r_deribit)
print(r_deribit.status_code)
print(type(r_deribit))
# print(r_deribit.text)
r_dict_deribit = r_deribit.json()
print(type(r_dict_deribit))
print()
print(r_dict_deribit)
print()
print()
best_bid_price = r_dict_deribit["result"]["best_bid_price"]
print("best_bid_price : ",best_bid_price)
bidss = r_dict_deribit["result"]["bids"]
print("bids : ",bidss)
print()
askss = r_dict_deribit["result"]["asks"]
print("asks : ", askss)
best_ask_prices = r_dict_deribit["result"]["best_ask_price"]
print("best_ask_price : ",best_ask_prices)
# deribit_json = json.dumps(r_dict_deribit, indent = 2)
# print(deribit_json)
