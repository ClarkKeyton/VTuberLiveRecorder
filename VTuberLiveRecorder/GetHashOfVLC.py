import hashlib

def getHashOf(filename : str):
    nashm = hashlib.md5()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            nashm.update(chunk)
        return nashm.hexdigest()