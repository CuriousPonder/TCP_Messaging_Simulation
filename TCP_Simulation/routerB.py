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
Port = 8081
source = "B"
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


def connectAthread():
    while True:
        try:

            sA.connect(("localhost", 8080))

            print("Router A is connected")

        except:
            continue


def connectCthread():
    while True:
        try:

            sC.connect(("localhost", 8082))

            print("Router C is connected")

        except:
            continue


def connectLthread():
    while True:
        try:
            # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sL.connect(("localhost", 8087))

            print("Router L is connected")

        except:
            continue




def conthread(conn, addr):
    #
    while True:
        try:

            pack = []
            i = 0
            while i == 0:
                # what are you? router or man or is it you chan?
                pack = conn.recv(1024)
                i = 1
            gainPack = pickle.loads(pack)
            print(gainPack)
            send_to = gainPack[1]

            if send_to == "jan":
                dest = "F"
                next = pathCalc(dest, source)
                if (next is "A"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sA.send(bytes(pack))
                            i = 1
                    except:
                        print("A does not exists")
                elif (next is "C"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sC.send(bytes(pack))
                            i = 1
                    except:
                        print("C does not exists")
                elif (next is "L"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sL.send(bytes(pack))
                            i = 1
                    except:
                        print("L does not exists")


            elif send_to == "ann":
                dest = "A"
                next = pathCalc(dest, source)
                if (next is "A"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sA.send(bytes(pack))
                            i = 1
                    except:
                        print("A does not exists")
                elif (next is "C"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sC.send(bytes(pack))
                            i = 1
                    except:
                        print("C does not exists")
                elif (next is "L"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sL.send(bytes(pack))
                            i = 1
                    except:
                        print("L does not exists")

            elif send_to == "chan":
                dest = "E"
                next = pathCalc(dest, source)
                if (next is "A"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sA.send(bytes(pack))
                            i = 1
                    except:
                        print("A does not exists")
                elif (next is "C"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sC.send(bytes(pack))
                            i = 1
                    except:
                        print("C does not exists")
                elif (next is "L"):
                    try:
                        # send (Username)(Send_to)(Message)
                        i = 0
                        while i == 0:
                            sL.send(bytes(pack))
                            i = 1
                    except:
                        print("L does not exists")

        except:
            print(addr, "disconnected")
            break
            # continue




sA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_thread.start_new_thread(connectAthread, ())
_thread.start_new_thread(connectCthread, ())
_thread.start_new_thread(connectLthread, ())

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