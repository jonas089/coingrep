'''
The Storage class is used to store user transactions and historical market data
Transactions are created through the CLI
'''
import pickle, time, os
from core.helpers.timestamp import unix_to_human, human_to_unix
from core.types import Transaction, MarketData

class Storage:
    def __init__(self, file_tx, file_mk):
        self.file_tx = file_tx
        self.file_mk = file_mk

    def initialize(self):
        if not os.path.exists(self.file_tx):
            open(self.file_tx, 'x')
        if not os.path.exists(self.file_mk):
            open(self.file_mk, 'x')

    def teardown(self):
        if os.path.exists(self.file_tx):
            os.remove(self.file_tx)
        if os.path.exists(self.file_mk):
            os.remove(self.file_mk)

    def insert_market_data(self, data, id):
        content = {}
        try:
            with open(self.file_mk, 'rb') as mk:
                content = pickle.load(mk)
        except Exception as exists:
            pass
        try:
            content[id].append(data)
        except Exception as empty:
            content[id] = [data]
        with open(self.file_mk, 'wb') as mk:
            pickle.dump(content, mk)

    def query_market_data(self, id):
        content = {}
        with open(self.file_mk, 'rb') as mk:
            content = pickle.load(mk)
        return content[id]