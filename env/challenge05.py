import pickle
import urllib.request

def challenge5(url):

    data = pickle.load(urllib.request.urlopen(url))

    for line in data:
        print("".join([k * v for k,v in line]))

    return None

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/banner.p"
    challenge5(url)
