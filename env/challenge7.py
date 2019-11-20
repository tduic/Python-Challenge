from PIL import Image
import requests, string
from io import BytesIO

def challenge7(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    data = list(img.getdata())
    gray = []
    i = 0
    y = data[0][0]
    s = ''
    print(string.printable)
    for p in data:
        if (p[0] == p[1] == p[2]) and (y == p[0]):
            i+=1
        else:
            if chr(y) in string.printable:
                s += chr(y)*((i+2)//6)
        i = 0
        y = p[0]
    print(s)


    # i = 0
    # y = data[0][0]
    # s = ''
    # for x in data:
    #     if (x[0] == x[1] == x[2]) and (y == x[0]): #a grey pixel and same as last pixel
    #         i+=1
    #     else:
    #         if chr(y) in (string.printable):
    #             s+=chr(y)*((i+2)//6) # make every dot 6 pixels wide
    #                                 # and show first only 4 pixels wide ‘s’ dot
    #     i = 0
    #     y = x[0]
    #     print(s)
    # bytestr = img.tobytes()
    # res = ''
    # for b in bytestr:
    #     c = chr(b)
    #     if c in string.ascii_letters:
    #         res += c
    # ans = ''
    # for i in range(len(res)-4):
    #     if res[i] == res[i+1] and res[i] == res[i+2] and res[i] == res[i+3]:
    #         ans += res[i]
    return None


if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    print(challenge7(url))
