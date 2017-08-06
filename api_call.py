import requests
from flask import jsonify

def get_price(json):

    orderBookBTC = "btc_cad"

    url = "https://api.quadrigacx.com/v2/ticker?book="

    getURL = url + orderBookBTC

    r = requests.get(getURL)

    #print(r.content)
    #print(r.text)

    if json == 1:
        return jsonify(r.json())

    else:
        return r.json()

