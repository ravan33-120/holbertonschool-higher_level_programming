#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1  # arqumentlərin sayı
    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print(f"{argc} arguments:")
        for i, arg in enumerate(argv[1:], 1):
            print(f"{i}: {arg}")
