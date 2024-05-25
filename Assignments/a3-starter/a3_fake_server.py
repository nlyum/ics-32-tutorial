import ds_client
import ds_protocol
import socket

def start_server(host_address, host_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((host_address, host_port))
        srv.listen()

        print(f"fake a3 server listening on ip address {host_address} port {host_port}")
        connection, address = srv.accept()

        with connection:
            print(f"client connected from {address[0]}")

            send = connection.makefile("w")
            recv = connection.makefile("r")
            
            while True:
                rec_msg = recv.readline()[:-1]

                print(f"message from client: {rec_msg}")

                if not rec_msg:
                    break
                    
                
                send.write(f"{address[0]} sent me " + rec_msg + "\r\n")
                send.flush()
                

            print("client disconnected")



if __name__ == "__main__":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    start_server(ip_address, 2020)