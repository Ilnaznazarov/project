import time
import random
import datetime
from socket import *
from threading import Thread

def pull2():
    text = 'succeful';
    temp1 = random.randint(20, 50)
    temp2 = random.randint(20, 50)
    temp3 = random.randint(20, 50)
    temp4 = random.randint(20, 50)

    napr = random.randint(2, 5)
    
    text = 'succeful' + ' ' + str(temp1) + ' ' + str(temp2) + ' ' + str(temp3) + ' ' + str(temp4) + ' ' + str(napr) + ' '
    text = str.encode(text)
    return text

def savedannie(x,y):
    now = datetime.datetime.now()
    text = str(x) +'_' + str(now.strftime("%d-%m-%Y")) + '.txt'
    f=open(text,'a')
    f.write(now.strftime("%H:%M:%S"))
    f.write(' ' + str(y) + ' ')
    f.close()

def saveoftime():
    while True:
        temp1 = random.randint(20, 50)
        temp2 = random.randint(20, 50)
        temp3 = random.randint(20, 50)
        temp4 = random.randint(20, 50)

        napr1 = random.randint(2, 5)
        napr2 = random.randint(2, 5)
        napr3 = random.randint(2, 5)
        napr4 = random.randint(2, 5)

        tok1 = random.randint(10, 20)
        tok2 = random.randint(10, 20)
        tok3 = random.randint(10, 20)
        tok4 = random.randint(10, 20)
        
        now = datetime.datetime.now()
    
        savedannie('temp1',temp1)
        savedannie('temp2',temp2)
        savedannie('temp3',temp3)
        savedannie('temp4',temp4)

        savedannie('napr',napr1)
        
        print('saveoftime')
        time.sleep(5)

th = Thread(target=saveoftime, args=())
th.start()

host = ''
port = 9090
addr = (host,port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)
#listen - запускает прием TCP
tcp_socket.listen(1)

#Бесконечный цикл работы программы
while True:
    #Если мы захотели выйти из программы
    print('wait connection...')
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    #устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    conn, addr = tcp_socket.accept()
    
    #recv - получает сообщение TCP
    data = conn.recv(1024)

    data1 = bytes.decode(data)
    data1 = data1.split()

    if data1:
        if (data1[0]=='time'):
            timedef=time.time()
            conn.send(pull2())

tcp_socket.close()
