import requests, json

def get_bitcoin_price(TX_PATH, MK_PATH, builder):
    id = "bitcoin"
    timeout = 5
    price = builder.simple_price([id], ["chf"])
    return json.loads(requests.get(price).text)["bitcoin"]["chf"]