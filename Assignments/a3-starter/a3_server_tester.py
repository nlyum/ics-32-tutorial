import ds_client
import ds_protocol

if __name__ == "__main__":
    address = "127.0.0.1"
    port = 2020
    username = "user2000"
    password = "pass"
    post_message = "message"

    ds_client.send(address, port, username, password, post_message)