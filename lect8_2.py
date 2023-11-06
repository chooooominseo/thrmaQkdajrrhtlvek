# 입력 암호화
"""
import getpass

pw = input("Pass :")
print(pw)
pw = getpass.getpass("Pass : ")
print(pw)
"""
"""
import hashlib

hl = hashlib.sha256()
target = "hello"

hl.update(target.encode("utf-8"))
"""
"""import Crypto.Hash.keccak as kek

target = "hello"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())

import platform as pf

pn = pf.uname()
pm = pf.machine()
pp = pf.processor()
ps = pf.system()

print(pn)

import urllib.request as ur

url = 'https://www.google.com'

res = ur.request.urlopen(url)
web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)"""
    
"""import http.client as hc

url = 'www.google.com'

conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulrp.html", "wb") as fp:
    fp.write(r.read())
    
import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)"""
    
import threading
import time

"""def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")
    
end = time.time()
print("single end", end - start)"""

"""
thread1 = threading.Thread(target=counter, args=("1num",))
thread2 = threading.Thread(target=counter, args=("2num", ))
thread3 = threading.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()"""

# 병렬 처리

import multiprocessing

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))

process1.start()
process2.start()
process3.start()

start = time.time()

process1.join()
process2.join()
process3.join()

end = time.time()
print("proc - end", end - start)