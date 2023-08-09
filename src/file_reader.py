import os

class FileData:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

def readFileData(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return FileData(filename, content)
    else:
        return None