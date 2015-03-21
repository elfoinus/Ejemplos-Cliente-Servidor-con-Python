# coding=utf-8
from __future__ import division
import socket
import thread
import sys
import time
import select
import uuid
import struct

HOST = '0.0.0.0'
SOCKET_LIST = []
RECV_BUFFER = 1024
PORT = 9000


class Client:
    pass


def operacion(a, b, op):
    if op == "SUMA":
        return a + b

    if op == "RESTA":
        return a - b

    if op == "MULTIPLICACION":
        return a * b

    if op == "DIVISION":
        if (b != 0):
            return a / b
        else:
            return False


def handler(client):
    """El handler maneja la conexión con cada socket individualmente"""

    print "Accepted connection from: ", client.addr

    # Este bucle se repite cada vez que se encuentran datos en el bufer
    while 1:

        # Leemos tamaño del bufer del socket cliente hasta recibir algo
        packet = client.socket.recv(RECV_BUFFER)

        # Unpack and do whatever
        # Sizes: https://docs.python.org/2/library/struct.html#format-characters
        # I = uns int: 4bytes
        # h = short: 2bytes
        # Ahora viene el packet en una string de longitud igual al primer valor
        try:

            data = struct.unpack("Ihh", packet[:8])
            # desde la pos 8 (I + 2*h) hasta longitud de la string del comando
            command = packet[8:8 + data[0]]
            print "Client " + client.code + ": " + "Command: " + str(command) + " - " + str(data) + "\nTotal clients: " + str(len(SOCKET_LIST))

            # Enviamos la informacion al cliente otra vez, si éste no nos la
            # devuelve es que se ha desconectado, entonces cerramos el socket
            # Debe ser una cadena de caracteres o un buffer
            resultado = "El resultado de la operacion es " + str(operacion(data[1],data[2],command))

            if not client.socket.send(resultado):
                client.socket.close()
                SOCKET_LIST.remove(client.socket)
                print "Client " + client.code + " not found - Socket closed - Total clients: " + str(len(SOCKET_LIST))
                break

        except:

            print "Excepcion en socket de cliente. Intentando cerrar la conexion"
            try:
                client.socket.close()
                SOCKET_LIST.remove(client.socket)
                print "Client " + client.code + " not found - Socket closed - Total clients: " + str(len(SOCKET_LIST))
                break
            except: 
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
        SOCKET_LIST.append(c.socket)

        # Y lo lanzamos en un hilo para gestionar su conexión
        thread.start_new_thread(handler, (c,))

    server_socket.close()

if __name__ == "__main__":
    sys.exit(server())
