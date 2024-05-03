import socket

def main():
    # Step 1: Creating a socket.
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Initiating a connection to a server using
    # the connect method of the socket object. It takes a 
    # single argument which is a tuple containing the server's
    # host names, and the port number that the server is
    # listening on

    my_socket.connect((socket.gethostname(), 6000))

    # Receiving data from the server and decoding it. The argument
    # 2048 specifies the maximum amount of that to receive in bytes.
    message = my_socket.recv(2048).decode("utf-8")

    print(f"Message from server: {message}")









if __name__ == "__main__":
    main()