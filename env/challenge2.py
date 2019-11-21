import string
from utils import readFile

def challenge2(path):
    content = readFile(path, "rt")
    res = ''
    for c in content:
        if c in string.ascii_letters:
            res += c
    return res

if __name__ == '__main__':
    print(challenge2("txt/challenge2.txt"))
