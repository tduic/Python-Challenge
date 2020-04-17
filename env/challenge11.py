from PIL import Image

def challenge11(img):
    im = Image.open(img)
    (w, h) = im.size

    even = Image.new('RGB', (w//2, h//2))
    odd = Image.new('RGB', (w//2, h//2))

    for i in range(w):
        for j in range(h):
            p = im.getpixel((i,j))
            if (i+j)%2 == 1:
                odd.putpixel((i//2, j//2), p)
            else:
                even.putpixel((i//2, j//2), p)
    even.show()
    odd.show()

if __name__== '__main__':
    path = "txt/challenge11.jpg"
    print(challenge11(path))
