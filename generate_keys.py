from Crypto.PublicKey import RSA


def generate_keys():
    key = RSA.generate(1024)
    private, public = key.exportKey(), key.publickey().exportKey()
    f = open("privatekey.key", "wb")
    f.write(private)
    f.close()
    f = open("publickey.key", "wb")
    f.write(public)
    f.close()


generate_keys()
