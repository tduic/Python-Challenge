import requests
import string

def challenge4Wrapper(nothing):

    def challenge4(origNothing):
        template = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
        response = requests.get(template + origNothing)
        resp = response.text
        nothing = ''

        for c in resp:
            if c in string.digits:
                nothing += c

        if len(nothing) < 3 or 6 < len(nothing):
            return origNothing

        return challenge4(nothing)

    return challenge4(nothing)

if __name__ == '__main__':
    nothing1 = "12345"
    print(challenge4Wrapper(nothing1))
    nothing2 = "8022"
    print(challenge4Wrapper(nothing2))
    nothing3 = "63579"
    print(challenge4Wrapper(nothing3))
