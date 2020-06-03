import xmlrpclib
import time

s = xmlrpclib.Server('http://localhost:8080')
s.set_beacon(1)

