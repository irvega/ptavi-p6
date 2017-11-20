#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

if len(sys.argv) != 3:
    sys.exit('Usage: python3 client.py method receiver@IP:SIPpor')

# Cliente UDP simple.
# Dirección IP del servidor.
LINE = sys.argv[2]
SERVER = '127.0.0.1'
SERVER2 = LINE.split('@')[1].split(':')[0]
print(SERVER2)
PORT = 6001
metodo = sys.argv[1]
# Contenido que vamos a enviar

  


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    print("Enviando: " + LINE)
    if metodo == 'INVITE':
        my_socket.send(bytes('INVITE sip:' + LINE + ' SIP/2.0\r\n', 'utf-8') 
                              + b'\r\n')
    if metodo == 'BYE':
        my_socket.send(bytes('BYE sip:' + LINE + ' SIP/2.0\r\n', 'utf-8') 
                              + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
