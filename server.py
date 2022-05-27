import socket
import time


host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

server_close = False
print("[ Server Started ]", host)

while not server_close:
    try:
        data, address = s.recvfrom(1024)

        if address not in clients:
            clients.append(address)

        current_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + address[0] + "]=[" + str(address[1]) + "]=[" + current_time + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if address != client:
                s.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        server_close = True

s.close()
