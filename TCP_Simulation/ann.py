
import socket
import sys
import _thread
import pickle
import random
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


IP_address = 'localhost'


seqNum = 0
ack = 0
header = '0x16'
drp = 0
ter = 0
urg = 0
rst = 0
syn = 0
fin = 0
receiver_win = '0x16'
checksum = 0
urg_pointer = ''

str_send = " "
print("Username: ")
username = ""

username = input("")
type(username)

#Used to calculate checksum
def calc_checksum(phrase):
    return '%2X' % (-(sum(ord(c) for c in phrase) % 256) & 0xFF)

def connectAthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sA.connect(("localhost", 8080))

            print("Router A is connected")

        except:
            continue

def connectEthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sE.connect(("localhost", 8084))

            print("Router E is connected")

        except:
            continue

def connectFthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sF.connect(("localhost", 8085))

            print("Router F is connected")

        except:
            continue

def connectHthread():
    while True:
        try:
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sH.connect(("localhost", 8088))

            print("Router H is connected")

        except:
            continue

sRec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sF = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sH = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if username == "chan":
    Port = int("001")
    sRec.bind((IP_address, Port))
    sRec.listen(10)
    _thread.start_new_thread(connectEthread, ())

elif username == "jan":
    Port = 100
    sRec.bind((IP_address, Port))
    sRec.listen(10)
    _thread.start_new_thread(connectFthread, ())
    _thread.start_new_thread(connectHthread, ())

elif username == "ann":
    Port = 111
    sRec.bind((IP_address, Port))
    sRec.listen(10)
    _thread.start_new_thread(connectAthread, ())
gainMessage = " "
def recFrom(conn, addr):
    while True:
        try :
            pack = []

            # print("here")
            i = 0
            while i == 0:
                # what are you? router or man or is it you chan?
                pack = conn.recv(1024)
                i = 1
            gainPack = pickle.loads(pack)
            print(gainPack)
            fromPerson = gainPack[0]
            send_to = gainPack[1]
            gainMessage = gainPack[2]
            print("MESSAGE FROM: ", fromPerson)
            print(gainMessage)
            if(gainMessage=='DEAD'):
                sys.exit()
                          
               
            
        except:
            
            print(addr, "disconnected")
            sys.exit()
            break
        

def recSide():
    while True:
        conn, addr = sRec.accept()
        

        result = _thread.start_new_thread(recFrom, (conn, addr))

    conn.close()
    recSide.close()




_thread.start_new_thread(recSide, ())


while str_send != "quit":

    pack = []
    #s.send(bytes(username.encode('utf-8')))

    print("Send to: ")
    str_send = input("")
    type(str_send)
    if str_send == "quit":
        sys.exit()
        break

    pack.append(username)
    pack.append(str_send)
    #s.send(bytes(str_send.encode('utf-8')))

    print("Message: ")
    message = input("")
    type(message)

    pack.append(message)

    if(message == str("EXECUTE")):
        seqNum = random.randint(1, 1000)
        ack = 1
        syn = 1
        urg = 1
        urg_pointer = '32° 43’ 22.77” N,97° 9’ 7.53” W'
        checksum = calc_checksum(message)
        pack.append(seqNum) 
        pack.append(ack) 
        pack.append(header) 
        pack.append(drp)
        pack.append(urg) 
        
        pack.append(rst)
        pack.append(syn) 
        pack.append(fin)
        pack.append(ter)
        pack.append(receiver_win)
        pack.append(checksum) 
        pack.append(urg_pointer)

        print('seqNum: ', seqNum)
        print('ACK: ',ack)
        print('SYN: ', syn)
        print('URG: ',urg)
        print('URG Pointer: ',urg_pointer)
        print('CheckSum: ',checksum)
        print('RST: ',rst)
        print('TER: ',ter)
        print('FIN: ',fin)
        print('Receiver Window: ',receiver_win)
        
    elif (message == str("CONGRATULATIONS")):
        seqNum = random.randint(1, 1000)
        ack = 1
        syn = 1
        urg = 1
        fin = 1
        urg_pointer = '32.76” N, -97.07” W '
        checksum = calc_checksum(message)
        pack.append(seqNum) 
        pack.append(ack) 
        pack.append(header) 
        pack.append(drp)
        pack.append(urg) 
        
        pack.append(rst)
        pack.append(syn) 
        pack.append(fin)
        pack.append(ter)
        pack.append(receiver_win)
        pack.append(checksum) 
        pack.append(urg_pointer)

        print('seqNum: ', seqNum)
        print('ACK: ',ack)
        print('SYN: ', syn)
        print('URG: ',urg)
        print('URG Pointer: ',urg_pointer)
        print('CheckSum: ',checksum)
        print('RST: ',rst)
        print('TER: ',ter)
        print('FIN: ',fin)
        print('Receiver Window: ',receiver_win)

    elif (message == str("CHAN DIED")):
        seqNum = random.randint(1, 1000)
        ack = 1
        syn = 1
        urg = 1
        fin = 0
        ter = 1
        rst = 1
        urg_pointer = 'TERMINATE CHAN'
        checksum = calc_checksum(message)
        pack.append(seqNum) 
        pack.append(ack) 
        pack.append(header) 
        pack.append(drp)
        pack.append(urg) 
        
        pack.append(rst)
        pack.append(syn) 
        pack.append(fin)
        pack.append(ter)
        pack.append(receiver_win)
        pack.append(checksum) 
        pack.append(urg_pointer)

        print('seqNum: ', seqNum)
        print('ACK: ',ack)
        print('SYN: ', syn)
        print('URG: ',urg)
        print('URG Pointer: ',urg_pointer)
        print('CheckSum: ',checksum)
        print('RST: ',rst)
        print('TER: ',ter)
        print('FIN: ',fin)
        print('Receiver Window: ',receiver_win)
    elif (username == 'chan' and message == 'DEAD'):
        seqNum = random.randint(1, 1000)
        ack = 1
        syn = 1
        urg = 1
        fin = 0
        ter = 1
        rst = 1
        urg_pointer = 'TERMINATE CHAN'
        checksum = calc_checksum(message)
        pack.append(seqNum) 
        pack.append(ack) 
        pack.append(header) 
        pack.append(drp)
        pack.append(urg) 
        
        pack.append(rst)
        pack.append(syn) 
        pack.append(fin)
        pack.append(ter)
        pack.append(receiver_win)
        pack.append(checksum) 
        pack.append(urg_pointer)

        print('seqNum: ', seqNum)
        print('ACK: ',ack)
        print('SYN: ', syn)
        print('URG: ',urg)
        print('URG Pointer: ',urg_pointer)
        print('CheckSum: ',checksum)
        print('RST: ',rst)
        print('TER: ',ter)
        print('FIN: ',fin)
        print('Receiver Window: ',receiver_win)
        
    else:
        seqNum = random.randint(1, 1000)
        ack = 1
        syn = 1
        urg = 0
        urg_pointer = ''
        checksum = calc_checksum(message)
        pack.append(seqNum) 
        pack.append(ack) 
        pack.append(header) 
        pack.append(drp)
        pack.append(urg) 
        
        pack.append(rst)
        pack.append(syn) 
        pack.append(fin) 
        pack.append(receiver_win)
        pack.append(checksum) 
        pack.append(urg_pointer)

        print('seqNum: ', seqNum)
        print('ACK: ',ack)
        print('SYN: ', syn)
        print('URG: ',urg)
        print('URG Pointer: ',urg_pointer)
        print('CheckSum: ',checksum)
        print('RST: ',rst)
        print('TER: ',ter)
        print('FIN: ',fin)
        print('Receiver Window: ',receiver_win)
    #s.send(bytes(message.encode('utf-8')))
    
    if (username == 'jan'):
        filename = username+ "_to_" + str_send+" log.txt"
        f = open(filename, "a+")
        f.write('[ %s : %s to %s || seqNum: %s,  ack: %s, header: %s, drp: %s, urg: %s, rst: %s, syn: %s, fin: %s, ter: %s, receiver_win: %s, checksum: %s, urg_pointer: %s] \n' % (username, message, str_send, seqNum, ack, header, drp, urg, rst, syn, fin, ter, receiver_win, checksum, urg_pointer))
    elif (username == 'ann'):
        filename = username+ "_to_" + str_send+" log.txt"
        f = open(filename, "a+")
        f.write('[ %s : %s to %s || seqNum: %s,  ack: %s, header: %s, drp: %s, urg: %s, rst: %s, syn: %s, fin: %s, ter: %s, receiver_win: %s, checksum: %s, urg_pointer: %s] \n' % (username, message, str_send, seqNum, ack, header, drp, urg, rst, syn, fin, ter, receiver_win, checksum, urg_pointer))
    elif (username == 'chan'):
        filename = username+ "_to_" + str_send+" log.txt"
        f = open(filename, "a+")
        f.write('[ %s : %s to %s || seqNum: %s,  ack: %s, header: %s, drp: %s, urg: %s, rst: %s, syn: %s, fin: %s, ter: %s, receiver_win: %s, checksum: %s, urg_pointer: %s] \n' % (username, message, str_send, seqNum, ack, header, drp, urg, rst, syn, fin, ter, receiver_win, checksum, urg_pointer))

    
    

    sendPack = pickle.dumps(pack)
    print(sendPack)
    try :
        if str_send == "H":
            sH.send(bytes(sendPack))
        elif username == "jan" :
            sF.send(bytes(sendPack))
        elif username == "chan" :
            sE.send(bytes(sendPack))
        elif username == "ann" :
            sA.send(bytes(sendPack))
        
    except:
        print("Can not connect to %s" % (str_send))
    

    """
    str_recv = s.recv(1024).decode('utf-8')
    str_send = ""
    print(str(str_recv))

    str_send = input("")
    type(str_send)
    if str_send == "quit":
        #sys.exit()
        break

    s.send(bytes(str_send.encode('utf-8')))

    str_recv = s.recv(1024).decode('utf-8')

    print(str(str_recv))
    """
f.close()
s.close()
