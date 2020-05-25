import socket

s = socket.socket()

result = s.connect_ex(('tannerbraithwaite.com', 444))

if(result ==0):
    print('Port is open')

else:
    print('Port is closed')
