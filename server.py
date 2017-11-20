#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion \r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("The client send " + line.decode('utf-8'))

            if ((line.decode('utf-8')).split(' ')[0]) == 'INVITE':
                self.wfile.write(b'SIP/2.0 100 Trying \r\n')

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit(' Usage: python3 server.py IP port audio_file')
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
