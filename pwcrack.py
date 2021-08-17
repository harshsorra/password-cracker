from binascii import hexlify
from hashlib import sha256
import time
count = 0
def hash_pword(salt, pword):
    assert(salt is not None and pword is not None)
    hasher = sha256()
    hasher.update(salt)
    hasher.update(pword.encode('utf-8'))
    return hasher.hexdigest()

hash_to_crack = input("enter the hash you want to crack: ")
wordlist = input("enter the wordlist you need to look into: ")
sp = hash_to_crack.split("$",1)
file = open(wordlist, 'r', encoding="ISO-8859-1")
words = file.read().splitlines()
t1_b = time.time()
for x in words:
    pword = x
    salt = sp[0].encode('utf-8')
    hashed_pword = hash_pword(salt, pword)
    hashed_pword = salt.decode('utf-8') + '$' + hashed_pword
    count += 1
    if hashed_pword == hash_to_crack:
        print("password found ", pword)
        break
t2_e = time.time()
total_time = t2_e - t1_b
gps = count/int(total_time)
print("no. of words ",count) 
print("total time in seconds is ",int(total_time)) 
print("no. of guesses per second is ",int(gps))  
