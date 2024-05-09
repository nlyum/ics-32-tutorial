#
# Example of urlib.parse
#
import sys
import urllib.parse


def decompose_url(url_name: str) -> None:
    parsed_url = urllib.parse.urlparse(url_name)
    # parsed_url is a named tuple
    print(parsed_url)
    print("Hostname: " + parsed_url.hostname)
    print("Scheme  : " + parsed_url.scheme)
    print("Path    : " + parsed_url.path)


if __name__ == "__main__":
    decompose_url(sys.argv[1])
