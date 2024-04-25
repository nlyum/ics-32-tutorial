import socket

#Importnt note: This code is showing how client-server work and does not contain
#error checking 

def main ():

    #Step 1) Creating a new socket object. 
    #Notes: 
    #SOCK_STREAM indicates that the socket will be used for 
    #TCP (Transmission Control Protocol) communication. 
    #socket.AF_INET specifies the address family for the socket (i.e. IPV4)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Step 2) we bind the socket to the specified host and port
    my_socket.bind ((socket.gethostname(), 6060))

    #Step 3) listen for incoming connecitons (i.e. from clients). 
    #s ready to accept incoming connections from client sockets, up to a maximum of 5 
    #queued connections. Once the number of queued connections reaches 5, additional 
    #connection attempts may be refused depending on the operating system's behavior
    my_socket.listen (5)

    #Steps 4 and 5: accept connections, and send/receive data  
    #The loops makes sure the server is infinitely running until it is explicitly stopped 
    while True:

        #Wait until a client connects to the server. When a connection is established, the accepts ()
        #function returns  a) new socket object which represents a connection, 
        #and b) the address of the client
        client_socket, address = my_socket.accept()

        print (f"Connected to client {address}")

        #After the connection is established, the server sends the message "Hello world!" 
        #to the client. It converts the string "Hello world!" into bytes using UTF-8 encoding 
        #before sending it.

        client_socket.send(bytes("Hello world!", "utf-8"))

        #Once the message is sent, the server closes the connection with the client by closing 
        #the client_socket. This means that the client and server are finished with their conversation.
        client_socket.close()


if __name__ == "__main__":
    main()