import socket
from _thread import *

host = '127.0.0.1'
portMain = 6000


sock = socket.socket()

sock.bind((host,portMain))

print("Starting to listen")

sock.listen(5)

def onNewClient(conn):
    msg="a"
    while msg:
        msg = conn.recv(1024).decode()
        conn.send(msg[::-1].encode())
    conn.close()
i=10

while True:
    conn, addr = sock.accept()
    start_new_thread(onNewClient, (conn,))
    print("connected to " + str(addr))
