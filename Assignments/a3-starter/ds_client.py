# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Nathan Lyum
# EMAIL: nlyum@uci.edu
# STUDENT ID: 63833693

import socket

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))
      
      send = client.makefile("w")
      recv = client.makefile("r")

      print(f"client connected to {server} on port {port}")
      json_msg = '{"join": {"username": ' + username + ', "password": ' + password + ', "token": ""}}'
      send.write(json_msg + "\r\n")
      send.flush()

      srv_msg = recv.readline()[:-1]
      print(f"response from server: {srv_msg}")
        
  except Exception as ex:
    print(f"Error: {ex}")
    return False
  else:
    return True
