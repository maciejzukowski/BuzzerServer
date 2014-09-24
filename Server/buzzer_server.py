#!/usr/bin/env python

from datetime import datetime
import signal
import serial
import socket
import json
import sys
import atexit

host = ''
port = 50001
backlog = 1
size = 1024
s = None
try:
    s = serial.Serial(port='/dev/tty.usbserial-A601F1TP',baudrate=9600,timeout=1)
    print 'ok'
except:
    print 'Issue with serial'
    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host,port)) 
server.listen(backlog)

def close_socket():
    print 'Closing'
    server.close()

atexit.register(close_socket)


data = json.dumps({'success':'1'})
response_headers = {
            'Content-Type': 'application/json;',
            'Content-Length': len(data),
            'Connection': 'close',
        }
response_headers_raw = ''.join("%s: %s\n" % (k, v) for k, v in response_headers.iteritems())
response_proto = 'HTTP/1.1'
response_status = '200'
response_status_text = 'OK\n' # this can be random

response = '%s %s %s' % (response_proto, response_status, response_status_text)
response = response + response_headers_raw + '\n' + data
print response

while 1: 
    client, address = server.accept()
    cfile = client.makefile('rw', 0)
    client.recv(size)
    print str(datetime.now()) + address.__str__()
    if s is None:
        try:
            s = serial.Serial(port='/dev/tty.usbserial-A601F1TP',baudrate=9600,timeout=1)
            count = 0
            while count < 5:
                s.write('Z')
                return_val = s.readline().strip()
                if return_val == "Pushed":
                    s.flushInput()
                    s.flushOutput()
                    cfile.write(response)
                    break;
                else:
                    print 'nothing1'
                    count += 1
            cfile.write('HTTP/1.0 400 Bad Request\n\n')
        except:
            cfile.write('HTTP/1.0 400 Bad Request\n\n')
            
    else:
        try:
            count = 0
            while count < 5:
                s.write('Z')
                return_val = s.readline().strip()
                if return_val == "Pushed":
                    s.flushInput()
                    s.flushOutput()
                    cfile.write(response)
                    break;
                else:
                    print 'nothing1'
                    count += 1
            cfile.write('HTTP/1.0 400 Bad Request\n\n')
        except Exception:
            cfile.write('HTTP/1.0 400 Bad Request\n\n')

    cfile.close()
    client.close()

