# Serve any data queried / pickled
from flask import Flask, request, jsonify
from constants import GECKO_HOST, GECKO_PORT
api = Flask(__name__)

@api.route('/', methods=['GET'])
def CoinGecko():
    return "Hello Gecko!"

def launch():
    api.run(threaded=True, host=GECKO_HOST, port=GECKO_PORT)