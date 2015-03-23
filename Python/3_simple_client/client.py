# coding=utf-8
import sys
import socket
import random
import time
import struct
import thread

HOST = '127.0.0.1'
RECV_BUFFER = 1024
PORT = 8082


def client():
    addr = (HOST, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.settimeout(60)
    client_socket.connect(addr)
    
    # Send starting position packet
    #thread.start_new_thread(send_position, (client_socket,0,0))

    while 1:

        # Read the local socket
        data = client_socket.recv(RECV_BUFFER)
        print data


if __name__ == "__main__":
    sys.exit(client())