#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.

# Dirección IP del servidor.


try:
    _, METODO, SIP_ADDRESS = sys.argv

except IndexError:
    sys.exit('Usage: client.py ip metodo sip_address')

SERVER,PORT = SIP_ADDRESS.split(':')
login,SERVER = SERVER.split('@')
print(SERVER,PORT,login)
PORT = int(PORT)
METODO = METODO.upper()
PROTOCOL = 'SIP/2.0\r\n'
DATA = ' '.join([METODO.upper(), "sip:" + SIP_ADDRESS, PROTOCOL])

# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    print("Enviando: " + LINE)
    my_socket.send(bytes(DATA, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
