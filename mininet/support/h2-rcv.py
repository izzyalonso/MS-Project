import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('10.0.2.2', 11999))

try:
    print "Accepting socket..."
    
    while True:
        data, addr = sock.recvfrom(4096)
        print "Read some data..."
        
        print "Got some data: %s" % data.decode()
        
        f_out = open("h2_in.txt", "a")
        f_out.write("Received: ")
        f_out.write(data.decode())
        f_out.write("\n")
        f_out.close()
    
except Exception as e:
    print e

sock.close()

