import json
import string
import requests
import pickle
import urllib.request
import zipfile, re
from PIL import Image

# def convert(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     ans = ''
#     for c in text:
#         if c not in alphabet:
#             ans += c
#         else:
#             ans += alphabet[(alphabet.find(c)+2)%26]
#     return ans

# print(map("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))

# print(map("http://www.pythonchallenge.com/pc/def/map.html"))

# url = "http://www.pythonchallenge.com/pc/def/channel.zip"

# response = requests.get(url)
# response.encoding = 'utf-8'

# print(zip(response.content))



# data = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

# for line in data:
#     print("".join([k * v for k,v in line]))

# def challenge4Wrapper(url):
#     num = 0
#     def challenge4(origURL, num):
#         print(num, origURL)
#         response = requests.get(origURL)
#         resp = response.text
#         nothing = ''
#         for c in resp:
#             if c in string.digits:
#                 nothing += c
#         url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
#         if num == 400:
#             return nothing
#         num += 1
#         challenge4(url, num)
#     return challenge4(url, num)

# print(challenge4Wrapper(url))

# def challenge3(text):
#     # Write your code here
#     res = ''
#     for i in range(3, len(text)-3):
#         ans = ''
#         tmp = 0
#         for j in range(9):
#             tmp = i + j - 4
#             if tmp >= 0 and tmp < len(text):
#                 ans += text[tmp]

#         cnt = 0
#         for k in range(len(ans)):
#             if i == 0:
#                 if (k == 3 or k == 7) and ans[k] not in string.ascii_lowercase: break
#                 if (k != 3 and k != 7) and ans[k] not in string.ascii_uppercase: break
#             if i == len(text)-4:
#                 if (k == 0 or k == 4) and ans[k] not in string.ascii_lowercase: break
#                 if (k != 0 and k != 4) and ans[k] not in string.ascii_uppercase: break
#             else:
#                 if (k == 0 or k == 4 or k == 8) and ans[k] not in string.ascii_lowercase: break
#                 if (k != 0 and k != 4 and k != 8) and ans[k] not in string.ascii_uppercase: break
#             cnt += 1

#         if cnt == len(ans):
#             # res.append(ans)
#             if i == 0:
#                 res += ans[3]
#             else:
#                 res += ans[4]
#     return res

# print(challenge3(response.text))

# def readFile(path):
#     print(path)
#     with open(path, "rt") as f:
#         content = f.read()
#     print(content)
#     writeFile("channel/content.txt", content)
#     newPath = ''
#     for word in content.split(" "):
#         for c in word:
#             if c not in string.digits:
#                 break
#         newPath = "channel/" + word + ".txt"
#     readFile(newPath)

# def writeFile(path, contents):
#     with open(path, "a") as f:
#         f.write(contents + '\n')

# print(readFile("channel/readme.txt"))

## 6 ##
# f = zipfile.ZipFile("channel.zip")
# num = "90052"
# comments = []
# while True:
#     content = f.read(num + ".txt").decode("utf-8")
#     print(content)
#     comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
#     match = re.search("Next nothing is (\d+)", content)
#     if match == None:
#         break
#     num = match.group(1)

#     print(" ".join(comments))


# lst = ['t', 'h', 'e', ' ', 'a', 'i', 'r']

# def permutation(lst):
#     if len(lst) == 0:
#         return []

#     if len(lst) == 1:
#         return [lst]

#     l = []
#     for i in range(len(lst)):
#        m = lst[i]
#        remLst = lst[:i] + lst[i+1:]
#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l

# for p in permutation(lst):
#     print(p)

## 7 ##
# url = "http://www.pythonchallenge.com/pc/def/oxygen.png"

# response = requests.get(url)
# response.encoding = 'utf-8'

# print(response.content)

# data = tuple(zip(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")))

# print(data)
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
