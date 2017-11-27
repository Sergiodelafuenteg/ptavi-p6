#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def check_method(self, method):
        methods = ['INVITE', 'ACK', 'BYE']
        self.data_send = ""
        if method in methods:
            if method == 'INVITE':
                print("gooooo")
                self.data_send = ("SIP 2.0 100 Trying\r\n\r\n" +
                                "SIP 2.0 180 Ringing\r\n\r\n" +
                                "SIP 2.0 200 OK\r\n\r\n")
            elif method == 'BYE':
                self.data_send = "SIP 2.0 200 OK\r\n\r\n"
            elif method == 'ACK':
                os.system('mp32rtp -i 127.0.0.1 -p 23032 < ' + 'cancion.mp3')
        else:
            self.data_send = "SIP 2.0 400 Bad request\r\n\r\n"
        self.wfile.write(bytes(self.data_send, 'utf-8'))
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        # Leyendo línea a línea lo que nos envía el cliente
        data = self.rfile.read().decode('utf-8')
        print(data.split(' '))
        metodo,sip_address,protocol = data.split(' ')
        self.check_method(metodo)
        print("El cliente nos manda " + metodo)
        self.data_send = "kokoko"

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
