import os

from encode.encode import encode, url_safe_encode

ROOT = os.getcwd()


def readfile(filename, mode=None):
    with open(filename, mode='r') as f:
        data = f.read()

        if mode == '-U':
            encoded = url_safe_encode(data)
            return encoded

        if mode is None:
            encoded = encode(data)
            return encoded


def writefile(data, filename='output.txt', mode=None):
    try:
        with open(filename, mode='x') as f:
            f.write(data)
    except FileExistsError as fe:
        print('File already exists!')


def readstring(string):
    encoded = encode(string)
    return encoded

