#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente que abre un socket a un servidor."""

import socket
import sys

try:
    _, METODO, SIP_ADDRESS = sys.argv

except IndexError:
    sys.exit('Usage: client.py ip metodo sip_address')

SERVER,PORT = SIP_ADDRESS.split(':')
login,SERVER = SERVER.split('@')
print(SERVER,PORT,login)
PORT = int(PORT)
METODO = METODO.upper()
PROTOCOL = 'SIP/2.0\r\n\r\n'
DATA = ' '.join([METODO.upper(), "sip:" + SIP_ADDRESS, PROTOCOL])


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", DATA)
    my_socket.send(bytes(DATA, 'utf-8'))
    data = my_socket.recv(1024)
    cod_answer = data.decode('utf-8').split(' ')[-2]
    if (cod_answer == '200') and (METODO != 'BYE'):
        DATA = ' '.join(["ACK", "sip:" + SIP_ADDRESS, PROTOCOL])
        my_socket.send(bytes(DATA, 'utf-8'))
        print(cod_answer)
    print('Recibido -- ', data.decode('utf-8'))

print("Fin.")
