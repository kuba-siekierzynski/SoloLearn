"""
RegEx prime checker

Coded by Kuba Siekierzynski (c) 2016
Original code:
https://code.sololearn.com/cgEoWC8lFuCk/#py

The code checks if a given number is prime using RegEx matching.

RegEx implemented here checks (tries to match) for "" and "1" (unary representation of 0 and 1) and then recursively checks for any instance of "11", "111", ..., "1"*n (unary representation of consecutive natural numbers)

Whenever such a string is matched, it looks whether the remaining part of the string consists only of multiple instances of this particular match.
In other words, it checks whether a unary representation of a number consists only of multiple unary representations of 2, 3 and so on. If at least one is true - the number is not prime, as it is a multiplication of another number.

"""

import re
def is_prime(n):
    return not bool(re.match(r"^1?$|^(11+?)\1+$", "1"*n))

num = int(input("Number to be checked: \n"))
print (num, "is" + " not" * (not is_prime(num)) +" a prime")
