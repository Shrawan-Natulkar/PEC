import hashlib

message = input("Enter a message: ")

sha_hash = hashlib.sha256(message.encode())

print("SHA-256 Hash:", sha_hash.hexdigest())
