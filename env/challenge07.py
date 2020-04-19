from PIL import Image
import requests, string
from io import BytesIO

def challenge7(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    data = list(img.getdata())
    w, h = img.size
    data = [data[i * w:(i + 1) * w] for i in range(h)]

    grayData = []
    grayH = range(43, 52) # gray boxes are only from h=43 to h=51
    grayW = range(0, 609, 7) # each box is 7px tall and they range from w=0 to w=608
    for i in grayH:
        for j in grayW:
            grayData.append(data[i][j])

    res = ''
    for p in grayData:
        res += chr(p[0])

    ans = ''
    numList = [105, 110, 116, 101, 103, 114, 105, 116, 121] # retrieved from response to above
    for num in numList:
        ans += chr(num)
    return ans


if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    print(challenge7(url))
