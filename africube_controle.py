import xmlrpclib
import time

s = xmlrpclib.Server('http://localhost:8080')
#s.set_freq(1000)
s.set_beacon(1)
i = 1
while True:
  print(i)
  time.sleep(2.4)
  s.set_beacon(0)
  print(i)
  time.sleep(2.4)
  s.set_beacon(1)
  print(i)
  i += 1
