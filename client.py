#!/usr/bin/env python

import socket
client_socket = socket.socket()
server_address='127.0.0.1'
server_port= 1987
client_socket.connect((server_address,server_port))
end_message = '\r\n\r\n'
message = raw_input('Enter a message: ')
message = message.rstrip() + end_message
data= (client_socket.send(message.encode('utf-8')))
print(data)
client_socket.close()