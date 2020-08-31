import socket
import ssl
                    #Assignment 4 OpenSSL
                    #Farhaan Jiwa and Ashlyn Schultz
                    #Modern Cryptography
                    #Professor Zheng
                    #27 March 2020
                    #This code was written independently by the team. 


listen_addr = '192.168.1.71'
listen_port = 3310
server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile = server_cert, keyfile = server_key)
context.load_verify_locations(cafile = client_certs)


bindsocket = socket.socket()
bindsocket.bind((listen_addr, listen_port))
bindsocket.listen(5)

while True:
    print("Waiting for client")
    newsocket, fromaddr = bindsocket.accept()
    print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
    conn = context.wrap_socket(newsocket, server_side=True)
    print("SSL established. Peer: {}".format(conn.getpeercert()))
    buf = b''  # Buffer to hold received client data

    while True:

            rcvdData = conn.recv(2048).decode()
            print ("C:",rcvdData)
            sendData = input("S: ")
            conn.send(sendData.encode())

            if(sendData == "Bye" or sendData == "bye"):

        
                print("Closing connection")
                break

conn.shutdown(socket.SHUT_RDWR)
conn.close()
#We ___Farhaan Jiwa and Ashlyn schultz____________ declare that I/We have completed this computer code completely and entirely on my/our own, without any consultation with others.  I/We have read the UAB Academic Honor Code and understand that any breach of the Honor Code may result in severe penalties.	
#Student signature(s)/initials: ____FJ and AS________	
#Date: _____04/29/2020_______
