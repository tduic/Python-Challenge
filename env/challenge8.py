import requests
import re
import codecs
import bz2

def challenge8(url):
    response = requests.get(url)
    resp = response.content
    comment = codecs.escape_decode(re.findall(b"<!--(.*?)-->", resp, flags = re.DOTALL)[0])[0]
    un = re.findall(b"\nun: '(.*?)'", comment)[0]
    pw = re.findall(b"\npw: '(.*?)'", comment)[0]
    user = bz2.decompress(un)
    pWord = bz2.decompress(pw)
    return (user, pWord)

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/integrity.html"
    print(challenge8(url))
