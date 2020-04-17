from PIL import Image

def challenge14(path1, path2):
    im2 = Image.open(path2)
    (w2,h2) = im2.size
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    out = Image.new('RGB', [100,100])
    x,y,p = -1,0,0
    d = 200
    while d/2 > 0:
        for v in delta:
            steps = d//2
            for s in range(steps):
                x, y = x + v[0], y + v[1]
                out.putpixel((x,y), im2.getpixel((p,0)))
                p += 1
            d -= 1
    out.save('txt/challenge14.jpg')

if __name__ == '__main__':
    path1 = "txt/challenge14_1.jpg"
    path2 = "txt/challenge14_2.png"
    print(challenge14(path1, path2))
