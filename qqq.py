from socket import AF_INET,socket,SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = '127.0.0.1'
PORT = 23456
BUFFERSIZE = 1024
ADDR = (HOST , PORT)
SERVER  = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

def gelen_mesaj():
    while True:
        client,client_adress = SERVER.accept()
        print("%s:%s baglandi." %client_adress)
        clients.send(bytes("cansukayalar.com Chat uygulaması \n" +
                           "adınızı girin :", "utf8"))
        adresses[client]= client_adress
        Thread(target=connect , args=(client,)).start()


def connect(client):
    isim=client.recv(BUFFERSIZE).decode("utf8")
    hosgeldin = "hosgeldin %s! cıkmak icin {cikis} yazınız " %isim
    
def yayin():
    pass


