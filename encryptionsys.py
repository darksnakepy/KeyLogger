from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encryption(key, text):
    cipher = PKCS1_OAEP.new(key)
    plaintext = text
    cipher_text = cipher.encrypt(plaintext)
    return cipher_text

def decryption(private_key, encryptedText):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(encryptedText)
    return decrypted_text

def exportPublicKey(filename, publicKey):
    with open(filename, 'wb') as f:
        f.write(publicKey.export_key())

def exportPrivateKey(filename, privatekey):
    with open(filename, 'wb') as f:
        f.write(privatekey.export_key())