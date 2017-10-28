"""
1000 Robots! v. 1.1

Coded by Kuba Siekierzyński (c) 2017

Robots are our friends! ;]

The code generates an image of a robot holding a welcome board.
"""

robot =\
'''          {0}
        {1}
       {2}({3} {3}){2}
         |=|
+----{4}-----{4}----+
|                   |
|  I am robot #{5}  |
|                   |
+------++---++------+
       {6}   {6}
      _{6}   {6}_
     (__|   |__)
'''

from random import randint, seed

def r(x):
    return x[randint(0, len(x)-1)]

hat1 = ['A', '_', '|', chr(220)]
hat2 = ['_/_\_', '_| |_', '(""")']
ears = ['"', "'", '*', '@']
eyes = ['•', '*', '-', '+', '^', '.', '~', 'o']
hand = ['"', "'", '|']
legs = ['[]', '()', '{}', '||', 'II']

# let's go!
s = randint(0, 999)
seed(s)
print(robot.format(r(hat1), r(hat2), r(ears), r(eyes), r(hand)*3, ('00'+str(s))[-3:], r(legs)))
