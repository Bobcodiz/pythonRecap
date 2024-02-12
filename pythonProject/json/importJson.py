import bookJson
import json

# s = json.dumps(bookJson.book)
# print(s)
#
# # to write into a remote file
# with open("./book.txt", "w") as b:
#     b.write(s)

#to read from thr file
read = open("./book.txt", "r")
f = read.read()
print(f)

#load it to a string

k = json.loads(f)
print(k)
b = k["bob"]
print(b)
