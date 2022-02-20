from ctypes import wintypes
import socket
import sys


def payload():
    path = input('Enter payload filepath here: ')
    p_file = open(path, 'rb')
    return p_file.read()

target_host = sys.argv[1]
target_port = 443
payload = payload()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, int(target_port)))
client.sendall(b'%s' % payload)

response = client.recv(4096)
print(response.decode())
