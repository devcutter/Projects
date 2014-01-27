from socket import *

HOST = '127.0.0.1'
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # client-side, connects to a host
while True:
    message = raw_input("Your Message: ")
    s.send(message)
    print "Awaiting reply"
    reply = s.recv(1024) # 1024 is max data that can be received print "Received ", repr(reply)
    print "Revceived", repr(reply)

s.close()
