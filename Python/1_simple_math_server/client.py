# coding=utf-8
import sys
import socket
import select
import random
import time
import struct
import os

HOST = '127.0.0.1'
RECV_BUFFER = 1024
PORT = 9000
OPERACIONES = ('SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION')


def client():
    addr = (HOST, PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(10)
    client_socket.connect(addr)

    while 1:
        # GENERAR UN PAQUETE CON 3 VALORES:
        # https://docs.python.org/2/library/struct.html#format-characters
        # 1 - Longitud de la string de operación: Unsigned Int 4byes
        # 2 - Valor 1: Short 2bytes
        # 3 - Valor 2: Short 2bytes
        # 4 - Operacion (SUMA-RESTA-MULTIPLICACION-DIVISION): String
        # Servidor devuelve resultado: Float

        # Python 3 ( random.choice(OPERACIONES), 'utf-8')

        op = random.choice(OPERACIONES)  # String to bytes
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        print "\nEnviando peticion de " + op + " para " + str(a) + " y " + str(b)
        packet = struct.pack("Ihh",len(op),a, b) + op
        client_socket.send(packet)
        # Hasta que no se recibe una respuesta del servidor
        # el cliente se queda en este bucle recv
        data = client_socket.recv(RECV_BUFFER)
        print data
        time.sleep(10)
        # os.system('cls') # Clean screen on windows


if __name__ == "__main__":
    sys.exit(client())
