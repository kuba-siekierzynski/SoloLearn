"""
How to use pickle module 🥒
Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cNXRdhIOg17U/#py

The code demonstrates in six simple steps how Python module 'pickle' can be used.

It .dumps() a dictionary into a file and later on .loads() and reads it from an opened pickle jar. The data is allocated to another variable (empty dictionary) to show how pickle preserves the data type and structure.

"""

import pickle, os
# os is NOT necessary for pickle to run, it's just for fun

capitals = {'Poland': 'Warszawa', 'Hungary': 'Budapest', 'Germany': 'Berlin', 'Sweden': 'Stockholm', 'Slovakia': 'Bratislava', 'Ukraine': 'Kyiv', 'Belarus': 'Minsk'}
# this dictionary will be pickled

cities = {}
# this dictionary will be filled with unjarred data

my_jar = 'my_jar.pickle'
# the file name (can be anything)

def make_jar(data): # packs data into a jar
    with open(my_jar, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def open_jar(data): # opens a jar
    try:
        with open(my_jar, 'rb') as f:
            data = pickle.load(f)
        print('*Success.', len(data), 'entries found.*')
        return data
    except FileNotFoundError:
        print('*File \'my_jar.pickle\' not found.*')
        quit()

# os-based methods, purely for directory checkup
def curr_dir(): # displays the current dir name
    return os.path.abspath(__file__)

def ls(): # lists all files in the current dir
    for subdir, dirs, files in os.walk('./'):
        for file in files:
            print (file)


# let's pickle some jars!
print('#'*27)
print('# Let\'s pickle some jars! #')
print('#'*27+'\n')
print('1. Pickling \'capitals\' into a jar...')
make_jar(capitals) # pickles capitals in a jar
print('*Pickled!*\n\n2. Let\'s check if the file was created.')
print('Local dir', curr_dir(), 'contains:')
ls()
print('\n3. OK. Let\'s try reading this file:')
f = open('my_jar.pickle', 'r')
for line in f:
    print(line)
f.close()
print('\n*Hmm... seems like we are looking through a jar and see only some pickled stuff. Not quite what we wanted...*')
print('\n4. Now let\'s open the jar with \'pickle\' and read it...')
cities = open_jar(capitals) # opens a jar and reads it
print('\n5. Jarred content was allocated to \'cities\'. Let\'s print it out:\n')
print(cities)
print('\n6. Now we\'re talking B) #likeaboss')
