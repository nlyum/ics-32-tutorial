import socket

def main ():

    #Step 1) creating a socket. 
    #See notes on the server side for creating a socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Step 2) Initiate a connection to a swerver using the connect() 
    #method of the socket object. It takes a single argument, which is a 
    #tuple containing the server's hostname (retrieved using socket.gethostname()) 
    #and the port number (6060) that the server is listening on.
    my_socket.connect((socket.gethostname(), 6060))


    #Reciving data from the server and decoding it. The argument 
    #2048 specifies the maximum amount of data to receive in bytes.
    message = my_socket.recv (2048).decode("utf-8")


    print (f"Message received: {message}")

if __name__ == "__main__":
    main()