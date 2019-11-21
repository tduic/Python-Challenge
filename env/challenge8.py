from utils import readFile

def challenge8():
    text = readFile("txt/challenge8.txt", "rt").split('\n')
    user, pword = text[0], text[1]

if __name__ == '__main__':
    print(challenge8())
