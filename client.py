#Client Program

import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect(("192.168.0.102", port))
#s.send("Hello server!")
f = open('python_chat-master.zip','rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
s.shutdown(socket.SHUT_WR)
f.close()
print "Done Sending"
print s.recv(1024)
s.close                     # Close the socket when done
