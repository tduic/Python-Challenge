from utils import readFile
import string, re

def challenge3(path):
    # Write your code here
    text = readFile(path, "rt")

    res = ''
    matches = re.findall("[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]", text)
    for match in matches:
        res += match[4]

    return res

if __name__ == '__main__':
    print(challenge3('txt/challenge3.txt'))
