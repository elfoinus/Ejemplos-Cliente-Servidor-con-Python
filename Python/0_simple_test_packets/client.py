# coding=utf-8
import sys
import socket
import select
import random
import time

HOST = '127.0.0.1'
RECV_BUFFER = 1024
PORT = 9000


def math_client():
    addr = (HOST, PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)

    while 1:
        """data = raw_input(">> ")
        if not data:
            break
        else:
            client_socket.send(data)
            data = client_socket.recv(RECV_BUFFER)
            print data"""
        client_socket.send("Test Packet")
        data = client_socket.recv(RECV_BUFFER)
        print data
        time.sleep(30);


if __name__ == "__main__":
    sys.exit(math_client())
