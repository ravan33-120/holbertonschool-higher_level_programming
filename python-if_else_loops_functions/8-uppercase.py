#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Kiçik hərfdirsə, böyük hərfə çeviririk, əks halda eyni qalır
        print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")
    print()
