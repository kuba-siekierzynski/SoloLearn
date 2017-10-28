"""
Remote directory download v. 1.0

Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cezlCwkWIF0E/#py

The code pulls down file content of a remote directory and downloads all files meeting certain search criteria.
Please make sure that you have all the rights to the remote directory!

The code was written as an answer to a thread at Sololearn, so it pulls .pdf files by default:
https://www.sololearn.com/Discuss/301037/pdf-file-download-from-web

"""

import urllib.request
import re

# replace the remote_dir with the desired remote directory address
remote_dir = 'http://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/'
url_path = urllib.request.urlopen(remote_dir)
real_path = url_path.read().decode('utf-8')

# replace the pattern with a RegEx proper syntax - currently set to find .pdf
file_pattern = re.compile("([\w\.-]+[\.]pdf)")
file_list = set(file_pattern.findall(real_path))
print(file_list)

for f in file_list:
    remote_file = urllib.request.urlopen(remote_dir + f)
    print('Copying file:', f, end='')
    local_file = open(f, 'wb')
    local_file.write(remote_file.read())
    local_file.close()
    print(' Done.')
    remote_file.close()

# Happy coding! :)
