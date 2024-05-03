import socket

def main():
    # Step 1: Creating a socket.
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Initiating a connection to a server
    my_socket.connect((socket.gethostname(), 6000))
    
    # this is our front-end code
    
    while True:
        user_input = input("Enter a string to capitalize (or Q to quit): ")

        if user_input.upper() == 'Q':
            break

        print(f"Sending user input to server: {user_input}")
        my_socket.send(user_input.encode("utf-8"))


        capitalized_string = my_socket.recv(2048).decode("utf-8")

        print(f"Message from server: {capitalized_string}")

    my_socket.close()



if __name__ == "__main__":
    main()