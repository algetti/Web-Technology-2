import socket
import time
from json import dumps
from threading import Thread

connections_array=[]
connect_time_array=[]
timer_starts_time=0
connections_amount=0
sockets=[]
connections_list={}
sock = socket.socket()
sock.bind(('', 5050))#прослушиваем сокет
sock.listen(18)

def sending(connections_array):
    for i in range(18):
        convert_to = dumps(connections_array) 
        sockets[i].send(convert_to.encode("utf-8"))
        i=i+1                
    print("18 seconds passed, data sent to clients, current time: ", time.ctime())

def timer(connections_array): 
    while time.process_time()<18: 
        do_nothing=0#do nothing  
    else:
        sending(connections_array

while True: 

    conn, addr = sock.accept()
    time.sleep(0.1) #задержка между отправками клиенту
    connections_amount=connections_amount+1  
    if connections_amount==1: #если первый клиент подьединился
        timer_starts_time=time.ctime() 
        print("first connections, timer starts at", timer_starts_time)
        th_1=Thread(target=timer, args=(connections_array,))
        th_1.start() 
        connections_array.append(timer_starts_time)
    connection_time=time.ctime()
    data = conn.recv(4096) 
    if not data:
        break
    print ("№",connections_amount,", client info: ", data.decode('utf-8'), addr
    print("connection time: ",connection_time,"\n")
    connections_list={"name: ": data.decode('utf-8'), "adress: ":addr,"connection time: ":connection_time } 
    connections_array.append(connections_list) 
    sockets.append(conn) 
