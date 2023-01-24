import hashlib

str1="pratheerth"
data=hashlib.md5()
final=data.hexdigest()
print(len(final))