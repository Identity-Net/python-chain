import json


class Block:
    def __init__(self, index, timestamp, transactions, keys, signature):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.keys = keys
        self.signature = signature
