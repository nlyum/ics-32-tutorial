import socket
def capitalizer(text):
    return text.upper()

def main():
    port = 6000
    
    # Step 1: create a new socket object
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Step 2: bind the socket to the specified host and port
    my_socket.bind((socket.gethostname(), port))

    # Step 3: Listen for incoming connections from clients
    my_socket.listen(5)

    print(f"server is listening on {socket.gethostname}:{port}")


    # Steps 4-5: accept connections and send/receive data
    while True:
        client_socket, address = my_socket.accept()

        print(f"Connected to client {address}")
        
        while True:
            client_data = client_socket.recv(2048).decode("utf-8").strip()
            print(f"Received data from client: {client_data}")

            # this checks to see if the received data is empty
            if not client_data:
                break
            
            # this is our back-end code
            capitalized_text = capitalizer(client_data)

            
            client_socket.send(capitalized_text.encode("utf-8"))

            # client_socket.send(bytes("Hello world!", "utf-8"))
        client_socket.close()
        

if __name__ == "__main__":
    main()