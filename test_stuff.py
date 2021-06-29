import json
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import DSS
from Crypto.Cipher import PKCS1_OAEP

from time import time
from blockchain import Blockchain

# get our private key
f = open("public.key")
private_key = f.read()
f.close()

# make a new chain
chain = Blockchain()


new_tx = chain.add_new_transaction("me", "you", 1)

rsa_private_key = RSA.importKey(private_key)
rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
encrypted_message = rsa_private_key.encrypt(str.encode("Mothra"))

newblock = chain.add_new_block(time(), encrypted_message)
print(chain.toJSON())
print(newblock)
# def main():
#     # add the public key to the chain
#     # the first block doesn't need a signature, so we can use it to add our genesis key
#     f = open("privatekey.key")
#     public_key = f.read()
#     f.close()
#     chain.add_new_key(public_key)
#     chain.add_new_block(time(), "")

#     # now let's try to add a new block. We will need a valid signature
#     new_block = chain.add_new_block(time(), "")
#     print(new_block)  # should print "invalid signature"

#     # and now with a valid signature
#     f = open("publickey.key")
#     private_key = f.read()
#     f.close()
#     # now we have the keys and can encrypt a message
#     message = str.encode("Mothra")
#     rsa_private_key = RSA.importKey(private_key)
#     rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
#     encrypted_message = rsa_private_key.encrypt(message)
#     # lets make a new block with the encrypted message as the signature
#     new_block = chain.add_new_block(time(), encrypted_message)
#     print(new_block)


# main()
