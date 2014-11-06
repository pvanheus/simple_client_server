#!/usr/bin/env python

import socket

client_socket = socket.socket()
# updated to talk to google
server_address='www.google.com'
server_port= 80
client_socket.connect((server_address,server_port))
message = 'GET http://www.google.com HTTP/1.0\r\n\r\n'
#message = message.rstrip() + end_message
data= (client_socket.send(message.encode('utf-8')))
print "data set, it was", data, "bytes"
reply = client_socket.recv(1024).decode('utf-8')
print reply
client_socket.close()