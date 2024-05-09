#
# POST example
#
import urllib.request
import json


def send_data(server_address: str, data: str) -> None:
    # create some data to send; we'll use json format
    json = {'data' : data}
    # properly encode the data for the request object
    data = urllib.parse.urlencode(json)
    data = data.encode('utf-8')
    # set a header, with content type. We don't need to specify user agent here
    # since we are just sending to a custom server. But this will be usually
    # necessary when dealing with most servers
    headers = {'content-type': 'application/json'}
    request = urllib.request.Request(server_address, data, headers)
    # make the call, and print the response
    response = urllib.request.urlopen(request)
    resp_data = response.read()
    response.close()
    print(resp_data)


if __name__ == '__main__':
    while True:
        data_to_send = input("What would you like to send? ")
        send_data(server_address="http://circinus-12.ics.uci.edu:8000",
                  data=data_to_send)
