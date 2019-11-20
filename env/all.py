import json
import string
import requests
import pickle
import urllib.request
import zipfile, re
from PIL import Image


url = "http://www.pythonchallenge.com/pc/def/channel.zip"

response = requests.get(url)
response.encoding = 'utf-8'

print(zip(response.content))



data = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in data:
    print("".join([k * v for k,v in line]))

def challenge4Wrapper(url):
    num = 0
    def challenge4(origURL, num):
        print(num, origURL)
        response = requests.get(origURL)
        resp = response.text
        nothing = ''
        for c in resp:
            if c in string.digits:
                nothing += c
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
        if num == 400:
            return nothing
        num += 1
        challenge4(url, num)
    return challenge4(url, num)

print(challenge4Wrapper(url))


def readFile(path):
    print(path)
    with open(path, "rt") as f:
        content = f.read()
    print(content)
    writeFile("channel/content.txt", content)
    newPath = ''
    for word in content.split(" "):
        for c in word:
            if c not in string.digits:
                break
        newPath = "channel/" + word + ".txt"
    readFile(newPath)

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents + '\n')

print(readFile("channel/readme.txt"))

## 6 ##
f = zipfile.ZipFile("channel.zip")
num = "90052"
comments = []
while True:
    content = f.read(num + ".txt").decode("utf-8")
    print(content)
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

    print(" ".join(comments))


lst = ['t', 'h', 'e', ' ', 'a', 'i', 'r']

def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

for p in permutation(lst):
    print(p)

# 7 ##
url = "http://www.pythonchallenge.com/pc/def/oxygen.png"

response = requests.get(url)
response.encoding = 'utf-8'

print(response.content)

data = tuple(zip(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")))

print(data)
filename = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")

with Image.open(filename) as image:
    width, height = image.size

def imageBits(file):
    try:
        #Relative Path
        img = Image.open(file)
        print(img.mode)

        #converting image to bitmap
        print(img.tobitmap())
    except IOError:
        pass

imageBits(filename)
