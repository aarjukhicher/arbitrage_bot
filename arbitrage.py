import requests
import json
class ClintArbitrage:
    def __init__(self):
        self.best_asks_cost = 0
        self.best_bid_cost = 0
        self.best_sell_price = 0
        self.best_buy_price = 0

    def deribit(self):
        deri_url ="https://test.deribit.com/api/v2/public/get_order_book?depth=5&instrument_name=BTC-PERPETUAL"
        deri_response = requests.get(deri_url)

        if deri_response.status_code ==200 :

            deribit_dict = deri_response.json()

            asks_prices = deribit_dict["result"]["asks"]
            print("asks_prices ",asks_prices)

            self.best_ask_cost = deribit_dict["result"]["best_ask_price"]
            print("best_ask_cost ",self.best_ask_cost)

            self.best_bid_cost = deribit_dict["result"]["best_bid_price"]
            print("best_bid_cost ",self.best_bid_cost)
        else:
            print("Something Wrong in url")
            return

    def bitmex(self):
        bitm_url ="https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBTUSD&depth=5"
        bitm_response = requests.get(bitm_url)

        if bitm_response.status_code ==200 :

            bitmex_list = bitm_response.json()
            # print("bitmex_list  ",bitmex_list)

            self.best_sell_price = bitmex_list[4]["price"]
            print("best_sell_price ",self.best_sell_price)

            self.best_buy_price =bitmex_list[5]["price"]
            print("best_buy_price ",self.best_buy_price)

        else:
            print("Something Wrong in url")
            return

    def arbitrage(self):

        if self.best_buy_price - self.best_asks_cost >= 5:
            print("Buy from Deribit and Sell Bitmex :- ")
        elif self.best_bid_cost - self.best_sell_price >= 5:
            print("Buy from Bitmex and Sell Deribit :- ")
        else :
            print("Pass")
            pass

if __name__=="__main__":
    obj = ClintArbitrage()

    obj.deribit()
    print()
    obj.bitmex()
    obj.arbitrage()