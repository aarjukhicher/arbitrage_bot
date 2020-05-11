import requests
import json

r_bitmex = requests.get("https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBTUSD&depth=5")
print(r_bitmex)
# print(r_bitmex.text)
r_bitmex_json = r_bitmex.json()
print(type(r_bitmex_json))
# print(r_bitmex_json)
symbols = r_bitmex_json[0]["symbol"]
print(r_bitmex_json)
print()
print()
price = r_bitmex_json[0]["price"]
print("symbol : ",symbols)
print("price : ",price,"  ",r_bitmex_json[0]["side"])
price = r_bitmex_json[4]["price"]
print("price : ",price,"  ",r_bitmex_json[4]["side"])
sell_price = r_bitmex_json[5]["price"]
print("price 5 : ",sell_price,"  ",r_bitmex_json[5]["side"])
sell_price = r_bitmex_json[9]["price"]
print("price 9 : ",sell_price,"  ",r_bitmex_json[9]["side"])