from core.storage import Storage
from core.types import Transaction
from rest.urls import UrlBuilder
from constants import MK_PATH, TX_PATH, API_BASE, API_COINS, API_SIMPLE, API_EXCHANGES
from examples.bitcoin_price import get_bitcoin_price
import requests, json

builder = UrlBuilder(API_BASE, API_COINS, API_EXCHANGES, API_SIMPLE)
btc = get_bitcoin_price(MK_PATH, TX_PATH, builder)
print("Bitcoin Price: {} CHF".format(btc))