import requests
import re

def challenge4(origNothing):
    template = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    nothing = origNothing
    while True:
        response = requests.get(template + nothing)
        resp = response.text
        print(resp)
        match = re.search("and the next nothing is (\d+)", resp)
        if match == None:
            break
        nothing = match.group(1)
    return None

if __name__ == '__main__':
    nothing1 = "12345"
    nothing2 = "8022"
    print(challenge4(nothing2))

