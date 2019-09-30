

# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import struct

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

i = 10

while i > 0:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    #print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))
    print ("Received %s bytes from %s %s: " % (len(buf), address, struct.unpack("i", buf)[0] ))
    i = i - 1
s.shutdown(1)
