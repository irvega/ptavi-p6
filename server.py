#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
import os
import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def error(self,line):
        line_error = line.split(' ')
        if len(line_error) !=3:
            fail = True
        if line_error[1] != 'sip:'
            fail =True
            
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion \r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            lista = ['INVITE', 'BYE', 'ACK']
            print("The client send " + line.decode('utf-8'))
            method = ((line.decode('utf-8')).split(' ')[0])
            if not line:
                break
            #if:
                self.wfile.write(b'SIP/2.0 400 Bad Request')
            if method == lista[0]:
                self.wfile.write(b'SIP/2.0 100 Trying \r\n')
                self.wfile.write(b'SIP/2.0 180 Ringing \r\n')
                self.wfile.write(b'SIP/2.0 200 OK  \r\n')
            elif method == lista[1]:
                self.wfile.write(b'SIP/2.0 200 OK  \r\n')
            elif method == lista[2]:
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 < ' + sys.argv[3]
                print("Vamos a ejecutar", aEjecutar)
                os.system(aEjecutar)
            elif method not in lista:
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed')
            # Si no hay más líneas salimos del bucle infinito


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit(' Usage: python3 server.py IP port audio_file')
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
