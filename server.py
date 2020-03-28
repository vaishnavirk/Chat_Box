import socket
import select
import sys
from _thread import *

server = "YOUR IPV4 ADDRESS"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

client_list = []


def clientThread(conn, addr):
    conn.send(str.encode("Welcome to this chatroom!"))

    while True:
        try:
            message = conn.recv(2048)
            print(message)
            broadcast(message,conn)
        except:
            continue


def broadcast(message, conn):
    for clients in client_list:
        if clients != conn:
            try:
                clients.send(message)
            except:
                clients.close()




while True:
    conn, add = s.accept()
    client_list.append(conn)

    print("connected to :", add[0])

    start_new_thread(clientThread,(conn, add))

conn.close()
s.close()


