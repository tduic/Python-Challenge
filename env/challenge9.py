import requests
import re
from utils import readFile

def challenge9(path):
    text = readFile(path, "rt")
    comment = re.findall("<!--(.*?)-->", text, flags=re.DOTALL)[0]
    first = re.findall("first:\n(.*?)\n\n", comment, flags=re.DOTALL)[0]
    second = re.findall("second:\n(.*?)\n\n", comment, flags=re.DOTALL)[0]
    print('first:', first)
    print('second:', second)
    return None

if __name__ == '__main__':
    path = "txt/challenge9.txt"
    print(challenge9(path))
