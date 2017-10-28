"""
Encrypt/decrypt text v. 1.0
Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cuKnuo01NOb9/#py

The code calls two methods for encryption and decryption of a sample text message. It goes a bit farther than a simple character replacement or ROT13-like methods.
Enjoy! :)

"""

# pprint handles proper printing in SL
from pprint import pprint

text = "A sample text to test encrypt()/decrypt() methods. The longer it stands, the more obvious it seems that it needs a proper, yet simple encryption/decryption method. This one here is pretty naive, but hard to guess at first, if you don't see the code :)"

def encrypt(txt):
    return ''.join(chr((ord(txt[i])+i)%256) for i in range(len(txt)))

def decrypt(txt):
    return ''.join(chr((ord(txt[i])-i)%256) for i in range(len(txt)))

# Encrypting the message...
enc = encrypt(text)
print('Encrypted message:\n'+'='*18+'\n')
pprint(enc)

# ...and now, let's try to decrypt it!
dec = decrypt(enc)
print('\nDecrypted message:\n'+'='*18+'\n')
print(dec)
