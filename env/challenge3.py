from utils import readFile
import string

def challenge3(path):
    # Write your code here
    text = readFile(path)

    res = ''
    for i in range(3, len(text)-3):
        ans = ''
        tmp = 0
        for j in range(9):
            tmp = i + j - 4
            if tmp >= 0 and tmp < len(text):
                ans += text[tmp]

        cnt = 0
        for k in range(len(ans)):
            if i == 0:
                if (k == 3 or k == 7) and ans[k] not in string.ascii_lowercase: break
                if (k != 3 and k != 7) and ans[k] not in string.ascii_uppercase: break
            if i == len(text)-4:
                if (k == 0 or k == 4) and ans[k] not in string.ascii_lowercase: break
                if (k != 0 and k != 4) and ans[k] not in string.ascii_uppercase: break
            else:
                if (k == 0 or k == 4 or k == 8) and ans[k] not in string.ascii_lowercase: break
                if (k != 0 and k != 4 and k != 8) and ans[k] not in string.ascii_uppercase: break
            cnt += 1

        if cnt == len(ans):
            # res.append(ans)
            if i == 0:
                res += ans[3]
            else:
                res += ans[4]
    return res

if __name__ == '__main__':
    print(challenge3('challenge3.txt'))
