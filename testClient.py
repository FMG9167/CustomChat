import socket, multiprocessing
 
host = '127.0.0.1'
portA = 5000

A = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

A.connect((host,portA))

def receive(s):
    msg=s.recv(2048).decode()
    while msg!="bye":
        print(msg)
        msg = s.recv(2048).decode()

# def send(s):
#     a=""
#     while a!="bye":
#         a=input()
#         s.send(a.encode())
#     s.send("bye".encode())


if __name__ == "__main__":
    # p1 = multiprocessing.Process(target=send, args=(A,))
    # p2 = multiprocessing.Process(target=receive, args=(A,))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    receive(A)