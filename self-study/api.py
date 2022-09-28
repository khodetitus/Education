import requests

"""
This program takes the price of Bitcoin from the Coinbase website...
 and informs me if the price of Bitcoin is below or equal to my ideal price. 
"""


def alert(price):
    print("hi masoud.btc price is good for buy")
    # If we had an SMS service from the Kaveh Nagar site, we can use this method to send SMS to us as well
    # Just put API KEY here
    API_KEY = ""
    url = "https://api.kavenegar.com/v1/API_KEY/sms/send/json"
    payload = {"receptor": "09120572655", "message": "price is as low as %i" % price}
    response = requests.post(url, data=payload)
    print(response)


my_ideal_price = 15000

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")
price = float(response.json()["data"]["amount"])
if price < my_ideal_price:
    alert(price)
