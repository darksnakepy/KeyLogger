from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encryption(public_key, data):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

# just in case we want to dump the keys
def exportPublicKey(filename, publicKey):
    with open(filename, 'wb') as f:
        f.write(publicKey)

def exportPrivateKey(filename, privatekey):
    with open(filename, 'wb') as f:
        f.write(privatekey.export_key())