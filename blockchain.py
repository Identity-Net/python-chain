from abc import abstractmethod
import json

from Crypto.Cipher import PKCS1_OAEP
from block import Block
from Crypto.Signature import DSS
from Crypto.PublicKey import ECC, RSA
from Crypto.Hash import SHA256


class Blockchain:
    def __init__(self):
        self.chain = self.start_chain()
        self.pendingTransactions = []
        self.pendingPublicKeys = []

    def start_chain(self):
        chain = []
        # Give the genesis block a hardcoded public key
        f = open("private.key")
        public_key = f.read()
        f.close()
        chain.append(Block(0, 0, [], [public_key], ""))
        return chain

    def add_new_block(self, timestamp, signature):
        new_block = Block(
            len(self.chain),
            timestamp,
            self.pendingTransactions,
            self.pendingPublicKeys,
            signature,
        )
        # Check that the signature is valid
        valid = self.is_valid_signature(signature)
        if not valid:
            return "invalid signature"
        self.chain.append(new_block)
        self.pendingPublicKeys = []
        self.pendingTransactions = []
        return new_block

    def is_valid_signature(self, signature):
        """
        we're going to take the signature and compare it to every public key
        that's been added in every block. If the decryption matches, it's valid
        """

        valid = False
        # If we only have the Genesis block, just return True
        if len(self.chain) < 1:
            return True
        # loop through the chain and get all of the keys
        keys = []
        for block in self.chain:
            for key in block.keys:
                keys.append(key)
        # loop through the keys and check if any of them is a valid match
        for key in keys:
            try:
                rsa_public_key = RSA.importKey(key)
                rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
                decrypted_message = rsa_public_key.decrypt(signature)
                print(decrypted_message)

                if decrypted_message == b"Mothra":
                    valid = True
            except Exception:
                print("exception")
        return valid

    def most_recent_block(self):
        return self.chain[-1]

    def add_new_transaction(self, sender, recipient, amount):
        self.pendingTransactions.append(
            {"sender": sender, "recipient": recipient, "amount": amount}
        )
        return self.pendingTransactions

    def add_new_key(self, key):
        self.pendingPublicKeys.append(key)
        return self.pendingPublicKeys

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__
            if not type(o) == bytes and not type(o) == set
            else str(o),
            sort_keys=True,
            indent=4,
        )
