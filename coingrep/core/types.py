import hashlib
from core.helpers.timestamp import unix_to_human, human_to_unix

class Transaction:
    def __init__(self, id, amount):
        self.id = id,
        self.amount = amount
        self.timestamp = time.time()
        
    def build(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "hash": hashlib.sha384("{}{}{}".format(self.id, self.amount, self.timestamp).encode('utf-8')).hexdigest()
        }

class MarketData:
    def __init__(self, id, timestamp, prices):
        self.id = id
        self.unix_timestamp = timestamp
        self.human_timestamp = unix_to_human(timestamp)
        self.prices = prices

    def build(self):
        return {
            "id": self.id,
            "unix_timestamp": self.unix_timestamp,
            "human_timestamp": self.human_timestamp,
            "prices": self.prices
        }