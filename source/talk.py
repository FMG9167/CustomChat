import socket, multiprocessing

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '127.0.0.1'
PORT = 7000

mysock.connect((IP,PORT))

connection=None

def receive(socket):
    socket.listen(1)
    c, addr = socket.accept()
    with open('talk/recv.txt') as r:
        r.write(addr)

    global connection
    connection = c
    
def sendCheck(sock):
    while True:
        with open('talk/send.txt', 'rw') as s:
            if s.read():
                sock.send(s.read())
                s.write("")
        


def send(connection, msg):
    socket.send(msg)

receiveThread = multiprocessing.Process(target=receive, args=(mysock,))
receiveThread.start()

checkSend = multiprocessing.Process(target=sendCheck, args=(mysock,))
