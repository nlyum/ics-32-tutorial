# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Nathan Lyum
# EMAIL: nlyum@uci.edu
# STUDENT ID: 63833693

import socket
import time
import ds_protocol
import ui

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
  #DONE: return either True or False depending on results of required operation

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
      client.connect((server, port))
      
      # print(f"client connected to {server} on port {port}")

      join_json_msg = join_json(username, password)
      
      # print(f"sending join json: {join_json_msg}")
      
      send = client.makefile("w")
      recv = client.makefile("r")

      send.write(join_json_msg + "\r\n")
      send.flush()

      resp = recv.readline()
      # print(f"response from server: {resp}")
      resp_type, resp_msg, resp_token = ds_protocol.extract_json(resp)
      print(f"{resp_msg}")

      if resp_type == "ok":
        if message:
          # print(f"sending message with token {resp_token}")
          send_post(client, resp_token, message)
        if bio:
          # print(f"sending bio with token {resp_token}")
          send_bio(client, resp_token, bio)
      elif resp_type == "error":
        return False
      
    except Exception as ex:
      print(f"Error: {ex}")
    else:
      return True
    return False
    
    
  

def send_post(client, token, msg):
  json_msg = post_json(token, msg)

  send = client.makefile("w")
  recv = client.makefile("r")

  send.write(json_msg + "\r\n")
  send.flush()

  resp = recv.readline()
  print(ds_protocol.extract_json(resp)[1])


def send_bio(client, token, bio):
  json_msg = bio_json(token, bio)

  send = client.makefile("w")
  recv = client.makefile("r")

  send.write(json_msg + "\r\n")
  send.flush()

  resp = recv.readline()
  print(ds_protocol.extract_json(resp)[1])


def join_json(username, password):
  return '{"join": {"username": "' + username + '", "password": "' + password + '", "token": ""}}'

def post_json(token, msg):
  return '{"token":"' + token + '", "post": {"entry": "' + msg + '","timestamp": "' + str(time.time()) + '"}}'

def bio_json(token, bio):
  return '{"token":"' + token + '", "bio": {"entry": "' + bio + '","timestamp": "' + str(time.time()) + '"}}'
