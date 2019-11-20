def readFile(path):
    with open(path, "rt") as f:
        content = f.read()
    return content
