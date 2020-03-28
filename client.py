import socket
import select
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverport = 5555

s.connect(('YOUR IPV4 ADDRESS', serverport))
# To receive that welcome msg

recv_msg = s.recv(1024)
print(recv_msg)

while True:
    message = input('type your msg here:')
    #message.encode()
    s.send( message.encode())
    recv_msg = s.recv(1024)
    print(recv_msg.decode())
s.close()

