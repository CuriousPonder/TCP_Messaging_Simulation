# TCP_Messaging_Simulation
Simulating server communication with multiple routers in Python.


Programming Language:
Python 3.6

IDE Used:
Jake: IDLE & CMD
Kev: PyCharm

Instructions:
Open all of the routers A-H, each one will wait to connect with each for complete network.
Open every client, ann, chan, and jan, then each one will connect to their respective server as the servers
will connect to the clients.
These connections only occur when entered their username.

The input format will follow:
Username:
(jan, chan, or ann)
Send To:
(jan, chan, or ann)
Message:
(input)

And it will send the packet to servers, representing routers based on given map.
Each router will execute a function to find the shortest path to reciever.
All information will be printed on server and client will print packets send and received.
Every packet sent will be documented in a text file (serving as the log) named (sender)_to_(receiver).txt.
If ann sends to chan DEAD, then chan will be disconnected from ann.
If ann sends jan EXECUTE, then jan can send to HQ (H) PEPPER THE PEPPER then with a response asking for the coordinates.
Jan can enter EXECUTE with embedded coordinates and H will reply with CONGRATULATIONS WE FRIED DRY GREEN LEAVES.
If ann sends CONGRATULATIONS to Jan, coordinates are sent to Jan in the packet for the next step

Format of the Packet:
[username, message, str_send, seqNum, ack, header, drp, urg, rst, syn, fin, ter, receiver_win, checksum, urg_pointer]

RESOURCES:

SOURCES USED TO DEVELOP THE CHAT ROOM BETWEEN CLIENT AND SERVER
https://www.geeksforgeeks.org/simple-chat-room-using-python/
https://stackoverflow.com/questions/36136937/why-doesnt-my-python-chat-client-show-the-data-that-the-server-is-sending-to-it
https://docs.python.org/3/howto/sockets.html
https://pythontips.com/2013/08/06/python-socket-network-programming/
https://www.binarytides.com/code-chat-application-server-client-sockets-python/
https://stackoverflow.com/questions/41621425/python-3-how-to-use-socket-to-create-a-simple-chat-program
https://github.com/dvatsav/Chat-Room-server/blob/master/client.py
https://docs.python.org/3.2/library/select.html
https://www.geeksforgeeks.org/socket-programming-python/
https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
https://www.tutorialspoint.com/python3/python_multithreading.htm
https://stackoverflow.com/questions/7501947/understanding-pickling-in-python

SOURCES USED FOR THE FILE IO/LOGS
https://www.tutorialspoint.com/python/python_files_io.htm
https://docs.python.org/3/tutorial/inputoutput.html

SOURCE USED FOR UNDERSTANDING HOW THE FLAGS WORK
https://github.com/Urinx/SomeCodes/tree/master/Python/tcp_ip

SOURCE USED FOR CHECKSUM
https://stackoverflow.com/questions/16822967/need-assistance-in-calculating-checksum
