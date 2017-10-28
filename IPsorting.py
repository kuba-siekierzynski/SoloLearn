"""
IP sorting with lambda - now works properly!
Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cJqu6Q00Gidt/#py

The code uses a lambda to sort a list of IP addresses stored as strings. The issue was the sorting had to be done not 'alphabetically', but 'numerically' - '192.X.X.X' should go AFTER '23.X.X.X', as 192 is greater than 23 (or 023, to be precise). Simple convert to string also doesn't work - if IP chunks are two- or one-digit, zeros are omitted and sorting fails.

"""

a = ['192.168.3.4', '23.45.5.67', '192.168.4.6', '30.25.55.0', '10.1.1.1', '212.3.67.89', '1.2.3.4']

a_sorted = sorted(a, key=lambda j: ''.join(('00'+j.split('.')[i])[-3::] for i in range(4)))

# lambda takes each of the list's items, splits it down on-the-fly with the dot as separator, adds zeros to chunks, if necessary, joins them back and treats it as the key for the sorted() method - so in short: 23 comes before 192, not after ;)

print(a_sorted)
