#! /usr/bin/python3

import socket
import time 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port = 52001
s.connect((host,port))

def ts(s):
   s.send('Africube de ZR6AIC TESTING AFSK MODE'.encode()) 
#   data = ''
#   data = s.recv(1024).decode()
#   print (data)
#   print ("s")


while True:
	ts(s)
	time.sleep(3)
	print (".")

#while 2:
#   r = input('enter')
#   ts(s)

s.close ()
