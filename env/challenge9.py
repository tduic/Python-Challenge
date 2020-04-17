import requests
import re
from utils import readFile
from PIL import Image, ImageDraw

def challenge9(path):
    text = readFile(path, "rt")
    comment = re.findall("<!--(.*?)-->", text, flags=re.DOTALL)[0]
    firstStr = re.findall("first:\n(.*?)\n\n", comment, flags=re.DOTALL)[0]
    secondStr = re.findall("second:\n(.*?)\n\n", comment, flags=re.DOTALL)[0]
    firstList = firstStr.split(',')
    first = list(map(int, firstList))
    secondList = secondStr.split(',')
    second = list(map(int, secondList))
    print('first:', first)
    print('second:', second)

    im = Image.new('RGB', (500,500))
    draw = ImageDraw.Draw(im)
    draw.polygon(first, fill='white')
    draw.polygon(second, fill='white')
    im.show()

    return None

if __name__ == '__main__':
    path = "txt/challenge9.txt"
    print(challenge9(path))
