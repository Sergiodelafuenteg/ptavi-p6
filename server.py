#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def check_method(self, method):
        methods = ['INVITE', 'ACK', 'BYE']
        if method in methods:
            pass

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            data = self.rfile.read().decode('utf-8')
            print(data.split(' '))
            #metodo,sip_address,protocol = data.split(' ')
            #self.check_method(metodo)
            print("El cliente nos manda " + data)

            # Si no hay más líneas salimos del bucle infinito
            if not data:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
