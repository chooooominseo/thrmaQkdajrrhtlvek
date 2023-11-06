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
import Crypto.Hash.keccak as kek

target = "hello"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())