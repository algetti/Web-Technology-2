import socket
import time

def users(i):
    Names = ["Name1","Name2","Name3","Name4","Name5","Name6","Name7","Name8",
                "Name9","Name10","Name11","Name12","Name13","Name14","Name15",
                "Name16","Name17","Name18"]
    return Names[i]

sock=[socket.socket() for i in range(18)]

for i in range (18):
    sock[i].connect((socket.gethostname(), 5050))
    sock[i].send(users(i).encode())

for i in range(18):
        data=sock[i].recv(4096)#запрашиваем 4096 бита
        print("user: ",users(i), "\n timer starts at: ", data.decode())



