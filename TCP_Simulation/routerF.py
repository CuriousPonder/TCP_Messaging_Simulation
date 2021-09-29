# Python program to implement server side of chat room.

import socket
import select
import sys

import threading
import _thread
import pickle
from minCalc import *

"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# takes the first argument from command prompt as IP address
IP_address = 'localhost'

# takes second argument from command prompt as port number
Port = 8085
source = "F"
print(source)

"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((IP_address, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)



list_of_clients = []

def connectLthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sL.connect(("localhost", 8087))

            print("Router L is connected")

        except:
            continue

def connectDthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sD.connect(("localhost", 8083))

            print("Router D is connected")

        except:
            continue

def connectJANthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            toJan.connect(("localhost", int("100")))

            print("Jan is connected")

        except:
            continue

def conthread(conn, addr):
    #
    while True:
        try:

            pack = []

            # print("here")
            i = 0
            while i == 0:
                # what are you? router or man or is it you chan?
                pack = conn.recv(1024)
                i = 1
            gainPack = pickle.loads(pack)
            print(gainPack)
            send_to = gainPack[1]

            if send_to == "jan" :
                dest = "F"
                try:
                    #send (Username)(Send_to)(Message)
                    i = 0
                    while i == 0:

                        toJan.send(bytes(pack))
                        i = 1


                except:
                    print("Jan does not exists")

            elif send_to == "ann" :
                dest = "A"
                next = pathCalc(dest, source)
                if (next is "L"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sL.send(bytes(pack))
                            i = 1
                    except:
                        print("L does not exists")
                elif (next is "D"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sD.send(bytes(pack))
                            i = 1
                    except:
                        print("D does not exists")

            elif send_to == "chan" :
                dest = "E"
                next = pathCalc(dest, source)
                if (next is "L"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sL.send(bytes(pack))
                            i = 1
                    except:
                        print("L does not exists")
                elif (next is "D"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sD.send(bytes(pack))
                            i = 1
                    except:
                        print("D does not exists")

        except:
            print(addr, "disconnected")
            break
            # continue


sL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
toJan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_thread.start_new_thread(connectLthread, ())
_thread.start_new_thread(connectDthread, ())
_thread.start_new_thread(connectJANthread, ())

while True:
    """Accepts a connection request and stores two parameters, 
    conn which is a socket object for that user, and addr 
    which contains the IP address of the client that just 
    connected"""

    conn, addr = server.accept()
    print("Connection Address(ip, port):" + str(addr))


    _thread.start_new_thread(conthread, (conn, addr))


conn.close()
server.close()
