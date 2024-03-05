import os

MK_PATH = './storage/mk.dat'
TX_PATH = './storage/tx.dat'

GECKO_HOST = os.getenv("GECKO_HOST", default='0.0.0.0')
GECKO_PORT = os.getenv("GECKO_PORT", default=8080)

API_BASE = 'https://api.coingecko.com/api/v3'
API_COINS = "{}/coins".format(API_BASE)
API_SIMPLE = "{}/simple".format(API_BASE)