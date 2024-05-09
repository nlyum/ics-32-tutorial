import socket


# Define the main method for the client
def main():
    # Define the server's address and port
    server_address = ("localhost", 8080)

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(server_address)

    # Send a simple HTTP GET request
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.sendall(request.encode())

    # Receive the response from the server
    response = client_socket.recv(1024)
    print(f"Received response:\n{response.decode()}")

    # Close the client socket
    client_socket.close()


if __name__ == "__main__":
    main()
