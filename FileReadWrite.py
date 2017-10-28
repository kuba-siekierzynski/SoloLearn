"""
File read/write in Python v. 1.0

Coded by Kuba Siekierzyński (c) 2017
Inspired by lars

This code shows how to save a modified list to a file and later retrieve it. Values are read as strings, get cleaned and converted to integers, which in turn are summed up.

The code is an answer to the thread below:
https://www.sololearn.com/Discuss/446080/

"""

Dataname = 'Textdoc.txt'
List = []
for i in range (0,100):
      List.append ('%2d \n'% (i))
f = open(Dataname,'w')
f.writelines (List)
f.close ()
print('The saved list equals to:', List)
# List was saved to the file

List2 =[]
f = open(Dataname, 'r')
List2 = f.readlines()
f.close()
print ('The retreived list equals to:', List2)
# List2 was read from the file

print ('Are lists equal?', List==List2)
# Lists are equal

Sum = 0
for i in List2:
    Sum += int(i.strip())
print('The sum equals to:', Sum)
# Sum equals to 4950
