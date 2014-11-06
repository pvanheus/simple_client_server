#!/usr/bin/env python

import socket
import argparse

parser = argparse.ArgumentParser('socket client')
parser.add_argument('--port', type=int, default=1987)
parser.add_argument('message_file', nargs='?', help='Optional file to read message from')
args = parser.parse_args()

if args.message_file != None:
    input_file = open(args.message_file)
    message = input_file.read()
else:
    message = raw_input('Enter a message: ')

client_socket = socket.socket()
server_address='127.0.0.1'
server_port= args.port
client_socket.connect((server_address,server_port))
end_message = '\r\n\r\n'
message = message.rstrip() + end_message
data= (client_socket.send(message.encode('utf-8')))
print(data)
reply = client_socket.recv(1024).decode('utf-8')
print "Got a reply:", reply
client_socket.close()