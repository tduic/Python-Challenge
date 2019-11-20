import zipfile, re
from utils import readFile

def getZip(start):
    f = zipfile.ZipFile("channel.zip")
    num = start
    comments = []
    while True:
        content = f.read(num + ".txt").decode("utf-8")
        comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
        match = re.search("Next nothing is (\d+)", content)
        if match == None:
            break
        num = match.group(1)
    print(" ".join(comments))
    return None

def challenge6(file):
    context = readFile(file, "rt")
    print(context)
    start = "90052"
    return getZip(start)

if __name__ == '__main__':
    challenge6("channel/readme.txt")
