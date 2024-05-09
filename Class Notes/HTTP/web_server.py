import socket
import threading


# Define a function to handle client connections
def handle_client(client_socket):
    # Receive the client's request
    request = client_socket.recv(1024)
    print(f"Received request: {request.decode()}")

    # Check if the request is for the root URL
    if request.startswith(b"GET / HTTP/1.1"):
        # Read the content of the index.html file
        with open("index.html", "rb") as file:
            content = file.read()

        # Send HTTP response with the content of index.html
        response = b"HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + content
        client_socket.send(response)
    else:
        # If the request is for other URLs, send a 404 Not Found response
        response = b"HTTP/1.1 404 Not Found\n\n404 Not Found"
        client_socket.send(response)

    # Close the client socket
    client_socket.close()


# Define the main method for the server
def main():
    # Define the server's address and port
    server_address = ("", 8080)

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind(server_address)

    # Start listening for incoming connections
    server_socket.listen(5)
    print("Listening on port 8080...")

    # Main server loop
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
