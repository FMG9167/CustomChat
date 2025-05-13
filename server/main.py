from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/dashboard')
@main.route('/dash')
def dash():
    return render_template('dash.html')





import socket, multiprocessing

host = '0.0.0.0'
port = 6000


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))

sock.listen(10)

def onNewClient(conn, addr):
    msg='a'
    while msg:
        msg = conn.recv(2048).decode()
        print(str(addr) + " >> " +msg)
    conn.close

def acceptClient(socket):
    connection , address  = socket.accept()
    proc = multiprocessing.Process(onNewClient, args=(connection, address))
    rec = multiprocessing.Process(acceptClient, args=(socket,))

    proc.start()
    rec.start()
    proc.join()
    rec.join()

acceptClient(sock)
