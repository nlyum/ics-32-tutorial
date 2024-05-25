import socket
def start_client(server_address, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_address, server_port))

        send = client.makefile("w")
        recv = client.makefile("r")
        
        print(f"fake client connected to {server_address} on {server_port}")
        
        while True:
            msg = input("enter message to send: ")
            send.write(msg + "\r\n")
            send.flush()

            srv_msg = recv.readline()[:-1]
            print(f"response from server: {srv_msg}")

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    start_client(ip_address, 2020)