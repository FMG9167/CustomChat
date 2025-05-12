import socket, multiprocessing, time
 
host = '127.0.0.1'
portA = 5000

A = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

A.bind((host,portA))

A.listen(1)

conn, _ = A.accept()

# def receive(s):
#     msg=s.recv(2048).decode()
#     while msg!="bye":
#         print(msg)
#         msg = s.recv(2048).decode()

def send(s):
    a='Connected'
    while a:
        s.send(a.encode())
        a=input()
    s.send("bye".encode())

def test():
    for i in range(0,10):
        print(i)
        time.sleep(2)

p1 = multiprocessing.Process(target=send, args=(conn,))
# p2 = multiprocessing.Process(target=receive, args=(conn,))
p3 = multiprocessing.Process(target=test)

p1.start()
# p2.start()
p3.start()

p1.join()
# p2.join()
p3.join()
