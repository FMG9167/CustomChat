import socket
 
host = '127.0.0.1'
portA = 6000

A = socket.socket()

try:
    A.connect((host,portA))
except socket.error as e:
    print(str(e))


def send(s):
    msg="Hello"
    while True:
        s.send(msg.encode('ascii'))
 
        # message received from server
        data = s.recv(1024)
 
        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :',str(data.decode('ascii')))
 
        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            msg=input("Enter input: ")
            continue
        else:
            break
    s.close()


if __name__ == "__main__":

    send(A)
