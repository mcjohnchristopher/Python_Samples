#USing Socket

import socket 
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect('www.google.com',80)
mysocket.connect('GET http://www.google.com/1.txt HTTP/1.0\n\n')
while true:
	data = mysocket.recv(512)
	if len(data) < 1 :
		break
	print data
mysocket.close()