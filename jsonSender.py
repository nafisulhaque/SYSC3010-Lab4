# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(type(y))

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

i = 10 #Counter

while i > 0:
    #print ("Enter data to transmit: ENTER to quit")
    data = json.dumps(y).strip()
    y["age"] = y["age"] + 1
    #data = random.randint(0, 255)
    #data = str(data).strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    #s.sendto(struct.pack("i", data), server_address)
    i = i - 1

s.shutdown(1)

