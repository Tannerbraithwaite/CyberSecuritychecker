import base64
bytes = bytearray("print('hello')", 'utf-8')

base64string = base64.b64enconde(bytes)

f = open('harmless.py', 'w')
f.write(base64string.decode('utf-8'))
