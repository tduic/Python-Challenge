def readFile(path, type):
    with open(path, type) as f:
        content = f.read()
    return content

def writeFile(path, type, content):
    with open(path, type) as f:
        f.write(content + '\n')
    return None
