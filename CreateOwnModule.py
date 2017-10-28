"""
Create your own module v. 1.0

Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cLF0P3C3eZ52/#py

Inspired by Given and Kasimayan :)
https://www.sololearn.com/discuss/645722/?ref=app

The code shows in a few steps how to create your own module in Python and later import a method from it. 

"""

import os
# that's just for checking the local path

print('*** How to create your own module? ***')
print('A PythonEdu guide by Kuba Siekierzynski')

print('\n1. Let\'s create a file \'my_module.py\':')

file_new = 'my_module.py'
# creates the module file

str = """
# my_module.py
# created by Kuba for SoloLearn
def my_method():
    print('''
    ####################################
    ##  This is a my_method() method  ##
    ## imported from my_module module ##
    ####################################
    ''')
"""
# this will be inserted into 'my_module.py'

file_handler = open(file_new, 'w')
file_handler.write(str)
file_handler.close()
print('*Done in the background*')
# ok, we have our file ready

print('\n2. Let\'s check the local path to see if the file was created:\n')
print('>>> os.listdir()\n', os.listdir())
# let's check the local path, should show 'source.py' and 'my_module.py'

print('\n3. Look what\'s inside the module:\n')
print('>>> open(\'my_module.py\', \'r\').read()')
file_handler = open(file_new, 'r')
print(file_handler.read())
file_handler.close()

print('4. Ok, we have our module ready. Let\'s try importing from it!\n')
from my_module import my_method
# should import the my_method from my_module
print('>>> from my_module import my_method')
print('*Done*')

print('\n5. Running the imported method...\n')
print('>>> my_method()')
my_method()
print('*It works!*')

print('\n6. This is basically how you create a module in Python!')
