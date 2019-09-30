# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import random, struct

random.seed()
host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

i = 10 #Counter

while i > 0:
    #print ("Enter data to transmit: ENTER to quit")
    #data = sys.stdin.readline().strip()
    data = random.randint(0, 255)
    #data = str(data).strip()
    #if not len(data):
    #    break
#    s.sendall(data.encode('utf-8'))
    #s.sendto(data.encode('utf-8'), server_address)
    s.sendto(struct.pack("i", data), server_address)
    i = i - 1

s.shutdown(1)

