"""
Inception-like file running v. 1.0

Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/c5f76DBYhYSO/#py

Inspired by learner :)

The code creates a file 'new.py' and puts Python-syntax instructions inside it. One of the instructions is to create another file 'script.py' and fill it with just one print statement. Then, run it inside.

So in SoloLearn the sequence goes:
source.py --> new.py --> script.py

"""

import os
# that's just for checking the local path

print('*** Ready for inception? Let\'s go! ***')
print('\n1. Let\'s check the local path:')
print(os.listdir())
# should list only the 'source.py' file

print('\n2. Now, let\'s create a new file and fill it with Python instructions:')

file_new = 'new.py'
# creates the first file

str = """
print ("# This is a statement inside \'new.py\' #")
f = open('script.py','w')
f.write(\'print(\"## and this is inside \\'script.py\\' ##\")\')
f.close()
print("*script.py fired by new.py*")
exec(open("script.py").read())
"""
# the set of instructions above will be inserted into 'new.py'

file_handler = open(file_new, 'w')
file_handler.write(str)
file_handler.close()
print('*Done*')
# ok, we have our file ready

print('\n3. Let\'s check the path again, to see if the file was created:')
print(os.listdir())
# let's check the local path, should show 'source.py' and 'new.py'

print('\n4. Seems alright. Now let\'s fire it up!')
print('*new.py fired*')
exec(open("new.py").read())
# should execute new.py which, in turn, creates and executes 'source.py'

print('\n5. The file was run successfully. It was supposed to create another file \'script.py\', fill it with a print instruction and run it.')

print('\n6. Let\'s check if the \'script.py\' file was indeed created:')
print(os.listdir())
# just to prove it was created alright

print('\n7. Now, let\'s see if the file is valid and does what we wanted:')
print('*script.py fired*')
exec(open("script.py").read())
# this proves it is  valid, normal file which stays on after execution

print('\n8. This is how running a script inside a script which creates another script and runs it looks like in Python! Imagine what would happen if you created an indefinite loop of self-creating scripts? A hint: file flood ;)')
