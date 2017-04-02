import socket              # Import socket module
import sys
import os

def main(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
    port = 8080                # Reserve a port for your service.

    s.connect(("192.168.1.92", port))
    s.sendall("swing")

    f = open('img.png','wb')

    print "Receiving..."
    l = s.recv(1024)
    while (l):
        print "Receiving..."
        f.write(l)
        l = s.recv(1024)
    f.close()
    print "Done Receiving"

    s.close                    # Close the socket when done

main([])
