#
# Simple web API example
#
import sys
import urllib.request
import json


def get_kanye_quote(url_name: str) -> None:
    # First we spoof an user agent
    headers = {'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like "
                             "Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                             "Gecko) CriOS/110.0.5481.83 Mobile/15E148 "
                             "Safari/604.1"}
    request = urllib.request.Request(url_name, data=None, headers=headers)
    # Now we can retrieve data
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response.close()
    # Parse the JSON that was received
    api_data_obj = json.loads(response_data)
    print("Type of parsed data: " + str(type(api_data_obj)))
    print("All retrieved data : " + str(api_data_obj))
    print("Retrieved quote    : " + api_data_obj['quote'])


if __name__ == "__main__":
    get_kanye_quote("https://api.kanye.rest/")
