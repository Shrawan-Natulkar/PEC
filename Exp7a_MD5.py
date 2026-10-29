import hashlib

message = input("Enter a message: ")

md5_hash = hashlib.md5(message.encode())

print("MD5 Hash:", md5_hash.hexdigest())
