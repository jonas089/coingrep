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