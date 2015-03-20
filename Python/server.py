# coding=utf-8
import socket
import thread
import sys
import time

HOST = '0.0.0.0'
SOCKET_LIST = []
RECV_BUFFER = 1024
PORT = 9000


class Client:
    pass


def handler(client):
    print "Accepted connection from: ", client.addr

    while 1:
        data = client.socket.recv(RECV_BUFFER)
        print "Client " + str(client.code) + ": " + data
        # send back the data
        client.socket.send(data)

    client.socket.close()


def math_server():

    server_addr = (HOST, PORT)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_addr)
    server_socket.listen(10)

    while 1:
        print "Server is listening for connections\n"
        time.sleep(1)
        c = Client()
        c.code = len(SOCKET_LIST)+1
        c.socket, c.addr = server_socket.accept()
        SOCKET_LIST.append(c.socket)
        thread.start_new_thread(handler, (c,))

    server_socket.close()

if __name__ == "__main__":
    sys.exit(math_server())
