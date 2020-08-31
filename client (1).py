import socket
import ssl

                    #Assignment 4 OpenSSL
                    #Farhaan Jiwa and Ashlyn Schultz
                    #Modern Cryptography
                    #Professor Zheng
                    #27 March 2020
                    #This code was written independently by the team.

host_addr = '192.168.1.71'
host_port = 3310
server_sni_hostname = 'www.farhaanjiwa.com'
server_cert = 'server.crt'
client_cert = 'client.crt'
client_key = 'client.key'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)

client_side_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(client_side_con, server_side=False, server_hostname=server_sni_hostname)
conn.connect((host_addr, host_port))
print("SSL established. Peer: {}".format(conn.getpeercert()))


while True:

    str = input("C: ")
    conn.send(str.encode()); 
    print (conn.recv(1024).decode())

    if(str == "Bye" or str == "bye"):

            print("closing connection")
            break
        
conn.close()

#We ___Farhaan Jiwa and Ashlyn schultz____________ declare that I/We have completed this computer code completely and entirely on my/our own, without any consultation with others.  I/We have read the UAB Academic Honor Code and understand that any breach of the Honor Code may result in severe penalties.	
#Student signature(s)/initials: ____FJ and AS________	
#Date: _____04/29/2020_______
