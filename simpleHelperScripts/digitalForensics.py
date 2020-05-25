import hashlib

file1 = open('/Users/tannerbraithwaite/github/python_scripts/CyberSecurityPrograms/oldfile.txt', 'r').read().strip().encode('utf-8')
file2 = open('/Users/tannerbraithwaite/github/python_scripts/CyberSecurityPrograms/newfile.txt', 'r').read().strip().encode('utf-8')

hash1 = hashlib.md5(file1).hexdigest()
hash2 = hashlib.md5(file2).hexdigest()

print(hash1 ==hash2)
