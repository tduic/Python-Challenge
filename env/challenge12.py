from PIL import Image
from utils import readFile

def challenge12(file):
    data = readFile(file, "rb")
    for i in range(5):
        open('%d.jpg' % i, 'wb').write(data[i::5])

if __name__ == '__main__':
    path = "txt/challenge12.gfx"
    print(challenge12(path))
