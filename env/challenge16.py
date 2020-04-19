from PIL import Image, ImageChops
import numpy as np

def challenge16(path):
    im = Image.open(path)
    mostFreq = max(enumerate(im.histogram()), key=lambda x: x[1])

    tmp = im.copy()
    tmp.frombytes(bytes([60] * (tmp.height * tmp.width)))
    # tmp.show()

    val = [x for x in im.histogram() if x % im.height == 0 and x != 0]
    index = im.histogram().index(val[0])

    tmp.frombytes(bytes([195] * (tmp.height * tmp.width)))

    shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(im)]
    Image.frombytes(im.mode, im.size, b"".join(shifted)).show()

if __name__ == '__main__':
    path = 'txt/challenge16.gif'
    print(challenge16(path))
