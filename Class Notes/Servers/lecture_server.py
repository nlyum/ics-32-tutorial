import socket


def main():
    # Step 1: create a new socket object
    # a socket is basically a string, much like a file
    # af_inet is the family of addresses
    # sock_stream indicates the socket will be used for TCP 
    # (Transmission Control Protocol)
    # TCP sends information in packets and lets you know that your
    # message was actually transmitted
    # socket.af_inet specifies the address family for the socket (IPV4)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Step 2: bind the socket to the specified host and port
    my_socket.bind((socket.gethostname(), 6000))

    # Step 3: Listen for incoming connections from clients
    my_socket.listen(5)
    # the server is now ready to accept incoming connections from client sockets
    # up to a maximum of 5 queued connections
    # once the number of queued connections is 5,
    # additional connections attempts will be refused
    # depending on the OS of the server

    # Steps 4-5: accept connections and send/receive data
    while True:
        # the server keeps listening until a client tries
        # to connect to the server. Once a connection is established,
        # the accept() method returns:
        # a) a new socket object, representing a connection
        # b) the address of the client
        client_socket, address = my_socket.accept()

        print(f"Connected to client {address}")

        # after the connection is established, the server sends the
        # message "Hello World" to the client,
        # it converts the string "Hello world!" to bytes
        # using utf-8 encoding before sending it

        client_socket.send(bytes("Hello world!", "utf-8"))

        # once the message is sent to the client, the server closes
        # the connection with the client by closing the 
        # client_socket object. this means that the client and
        # the server are finished with their conversation
        client_socket.close()
        



if __name__ == "__main__":
    main()