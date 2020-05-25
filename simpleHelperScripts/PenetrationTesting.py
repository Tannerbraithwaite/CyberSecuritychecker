import requests

response = requests.get('http://tannerbraithwaite.com')

print(response.text)
if(response.status_code == 200):
    response = requests.get('http://tannerbraithwaite.com')
    if(response.status_code == 200):
        print('vulnerable site')
    else:
        print(response.status_code)
        print('not a vulnerable site')
else:
    print('Request failure')
