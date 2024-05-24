import socket
def start_client(server_address, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_address, server_port))

        send = client.makefile("w")
        recv = client.makefile("r")
        
        print(f"fake client connected to {server_address} on {server_port}")
        msg = input("enter message to send: ")
        send.write(msg + "\r\n")
        send.flush()

        srv_msg = recv.readline()[:-1]
        print(f"response from server: {srv_msg}")

if __name__ == "__main__":
    start_client("127.0.0.1", 2020)