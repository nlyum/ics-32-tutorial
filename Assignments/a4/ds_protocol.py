# ds_protocol.py

# NAME: Nathan Lyum
# EMAIL: nlyum@uci.edu
# STUDENT ID: 63833693

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
# DONE: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['type', 'message', 'token'])

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  DONE: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    json_obj = json.loads(json_msg)
    type = json_obj['response']['type']
    message = json_obj['response']['message']

    if 'token' in json_obj['response']:
      # print(f"JSON string: {json_obj}")
      token = json_obj['response']['token']
    else:
      token = ''
    
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(type, message, token)
