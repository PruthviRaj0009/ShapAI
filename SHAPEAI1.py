import hashlib

print("Enter a String: ", end="")
value = input()

result = hashlib.md5(value.encode())

print("The byte equivalent of hash is : ", end="")
print(result.digest())
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
