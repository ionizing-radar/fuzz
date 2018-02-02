#!/usr/bin/python
import socket
import sys
if len(sys.argv) != 3:
 print "Usage: smbvrfy.py <input_file> <username>"
 sys.exit(0)

server_list = open(sys.argv[1]).read().split('\n')

for mail_server in server_list:

   # Create a server socket
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   print mail_server

   connect=s.connect((mail_server,25))

   # Receive the banner
   banner=s.recv(1024)
   print banner
   # VRFY a user
   s.send('VRFY ' + sys.argv[2] + '\r\n')
   result=s.recv(1024)
   print result
   # Close the socket
   s.close()

