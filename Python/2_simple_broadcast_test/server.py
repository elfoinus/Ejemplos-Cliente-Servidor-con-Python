# coding=utf-8
import socket
import thread
import sys
import time
import struct
import uuid

HOST = '0.0.0.0'
SOCKET_LIST = []
RECV_BUFFER = 1024
PORT = 9000

class Client:
    pass

def handler(client):
    """El handler maneja la conexión con cada socket individualmente"""

    print "Accepted connection from: ", client.addr

    # Este bucle se repite cada vez que se encuentran datos en el bufer
    while 1:

        try:
            packet = client.socket.recv(RECV_BUFFER)
            data = struct.unpack("hh", packet)

            # Hacemos un broadcast de lo que dice el cliente a todos los demás
            # clientes
            for c in SOCKET_LIST:
                # a los clientes enviamos la actual del cliente lol
                if not c.socket.send(client.code + " " + str(data)):
                    try:
                        c.socket.close()
                    finally:
                        SOCKET_LIST.remove(c)
                        print "Client " + c.code + " not found - Socket closed"
                        break

            print "Total clients: " + str(len(SOCKET_LIST))

        except Exception as e:
            print "Excepcion en socket de cliente:"
            print e
            try:
                client.socket.close()
            finally:
                SOCKET_LIST.remove(client)
                print "Client " + client.code + " not found - Socket closed - Total clients: " + str(len(SOCKET_LIST))
                break   
    return


def server():

    # Declaración del socket
    server_addr = (HOST, PORT)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_addr)
    server_socket.listen(10)

    print "Server is listening for connections\n"
    while 1:

        # Esto ocurre antes de que se conecte un nuevo cliente
        c = Client()
        c.code = str(uuid.uuid4().fields[-1])[:5]

        # El server se queda en el bucle server_socket.accept()
        # hasta que se conecte un cliente y entonces se devuelven
        # el socket y la direccion desde donde se ha conectado
        c.socket, c.addr = server_socket.accept()

        # Lo añadimos a una lista
        SOCKET_LIST.append(c)

        # Y lo lanzamos en un hilo para gestionar su conexión
        thread.start_new_thread(handler, (c,))

    server_socket.close()

if __name__ == "__main__":
    sys.exit(server())
