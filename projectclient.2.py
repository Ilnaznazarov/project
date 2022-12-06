import time
import os.path
import datetime
from socket import *
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

window = Tk()  
window.title("Приложение ЭЙАРСИ для управления роботом")  
window.geometry('700x550')  

def grafic(x):
    text = x + '_' + str(now.strftime("%d-%m-%Y")) + '.txt'

    f=open(text,'r')
    result = f.read().split()
    i = 0
    y = []
    x = []
    while (i<len(result)):
        x.append(result[i])
        y.append(int(result[i+1]))
        i= i+2

    i=0
    x = [datetime.datetime.strptime(i, "%H:%M:%S") for i in x]
    plt.plot(x,y)
    
    plt.xlabel("Время")
    plt.ylabel("Температура 1")

    plt.grid(which='major')
    
    plt.show()
    
    f.close()

l1 = Label(text="Наличие связи :", font="Arial 12")
l1.place(x=20,y=20)

btn1 = Button(window, text="Температура 1: " , command= lambda: grafic('temp1'))
btn1.place(x=20,y=130)

btn2 = Button(window, text="Температура 2: " , command= lambda: grafic('temp2'))
btn2.place(x=20,y=160)

btn3 = Button(window, text="Температура 3: " , command= lambda: grafic('temp3'))
btn3.place(x=20,y=190)

btn4 = Button(window, text="Температура 4: " , command= lambda: grafic('temp4'))
btn4.place(x=20,y=220)

btn5 = Button(window, text="Напряжение 1: " , command= lambda: grafic('napr'))
btn5.place(x=20,y=250)


def savedannie(x,y):
    now = datetime.datetime.now()
    text = srt(x) + '_' + str(now.strftime("%d-%m-%Y")) + '.txt'
    f=open(text,'a')
    f.write(now.strftime("%H:%M:%S"))
    f.write(' ' + data1[1] + ' ')
    f.close()

def pull1():
    while True:
        try:
            host = '192.168.0.5'
            port = 9090
            addr = (host,port)
            tcp_socket = socket(AF_INET, SOCK_STREAM)
            data='time'
            tcp_socket.connect(addr)
            #encode - перекодирует введенные данные в байты, decode - обратно
            data = str.encode(data)
            tcp_socket.send(data)
            data = tcp_socket.recv(1024)

            data1 = bytes.decode(data)
            data1 = data1.split()

            tcp_socket.close()
            
            if (data1[0]=='succeful'):
                l1.config(text = "Наличие связи : Есть")
                btn1.config(text = "Температура 1: " + str(data1[1]))
                btn2.config(text = "Температура 2: " + str(data1[2]))
                btn3.config(text = "Температура 3: " + str(data1[3]))
                btn4.config(text = "Температура 4: " + str(data1[4]))
                btn5.config(text = "Напряжение: " + str(data1[5]))
                
                savedannie('temp1',data1[1])
                savedannie('temp2',data1[2])
                savedannie('temp3',data1[3])
                savedannie('temp4',data1[4])

                savedannie('napr1',data1[5])
                savedannie('napr2',data1[6])
                savedannie('napr3',data1[7])
                savedannie('napr4',data1[8])

                savedannie('tok1',data1[9])
                savedannie('tok2',data1[10])
                savedannie('tok3',data1[11])
                savedannie('tok4',data1[12])
            
            time.sleep(5)
        except:
            l3.config(text = "Наличие связи : Отсутсвует")
            time.sleep(5)
            pass
