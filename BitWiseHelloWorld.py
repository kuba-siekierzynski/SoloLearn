"""
Bitwise Hello World v. 1.2
Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cevCloev897h/#py

A yet newer approach to the old problem :)
(now without the unnecessary if statement and another line reduced)

Check out the RUBY version, too:
https://code.sololearn.com/c0JtSdjYN2Oc/?ref=app

"""

k = [18325766, 18096393, 32973065, 18096393, 18333158, 0, 18037006, 18130185, 22329609, 22325513, 10692078]

for j in k:
    for i in range(25):
        print(chr(176 + bool(j & 2**(24-i)) * 43), end='\n'*(i//24))
