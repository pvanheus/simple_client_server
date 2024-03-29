#!/usr/bin/env python

import socket
import select
import argparse

parser = argparse.ArgumentParser('simple socket')
parser.add_argument('--port', type=int, default=1987, help='port to listen on')
args = parser.parse_args()

server_socket = socket.socket()
server_name = '127.0.0.1'
server_port = args.port
server_socket.bind((server_name,server_port))
server_socket.listen(5)
timeout = 60
block_size = 1024

while True:
    c , address = server_socket.accept()
    print("WE GOT CONNECTION FROM",address)
    message_done = False
    message = ''
    c.setblocking(0)
    while not message_done:
        ready_to_read = select.select([c],[],[], 60)[0]
        print "ready to read:", ready_to_read
        if ready_to_read != None:
            socket = ready_to_read[0]
            print "lets go read"
            data = socket.recv(block_size).decode('utf-8')
            print "got data"
            message += data
            if '\r\n\r\n' in data:
                print "the message is:", message
                message_done = True
    print "the message we got was:", message
    c.send("here is my reply, thank you".encode('utf-8'))
    c.close()
server_socket.close()