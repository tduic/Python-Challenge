import re

def challenge10():
    string = '1'
    for i in range(30):
        string = ''.join([str(len(i+j))+i for i,j in re.findall(r'(\d)(\1*)', string)])
    return len(string)

if __name__ == '__main__':
    print(challenge10())
