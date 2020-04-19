from string import *
a = ascii_lowercase

def challenge1(text):
    table = str.maketrans(a, a[2:] + a[:2])
    return text.translate(table)

if __name__ == '__main__':
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(challenge1(text))
    url = "map"
    print(challenge1(url))

