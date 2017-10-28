"""
Fizz Buzz Woof v. 1.0
Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cnohYAdJ69ik/#py

The code is a simple demonstration of the popular children's game. In an enumeration, every number divisible by 3, 5 or 7 gets replaced by Fizz, Buzz or Woof, respectively.
Multiple divisibility produces multiple replacements, so 21 (divisible by both 3 and 7) gets replaced by Fizz Woof.

"""

fbw = {3: 'Fizz', 5: 'Buzz', 7: 'Woof'}
# dictionary holding the divisors and their replacements

for i in range(1, 106):
# checking up to 105, as it's the first occurence of Fizz Buzz Woof :)
    repl = False # does the number need to be replaced?
    for j in fbw:
        if i%j == 0: # if the number is divisible by at least one fbw divisor
            repl = True # replacement is needed
            print(fbw[j], end=' ') # print the replacement from the dictionary
    if not repl:
        print(i, end='') # if there was no fbw found, just print the number
    print()
