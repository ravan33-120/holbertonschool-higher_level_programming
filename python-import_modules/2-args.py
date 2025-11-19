#!/usr/bin/python3
from sys import argv

if **name** == "**main**":
argc = len(argv) - 1  # arqumentlərin sayı (argv[0] skriptin adı olduğu üçün çıxır)
if argc == 0:
print("0 arguments.")
else:
if argc == 1:
print("1 argument:")
else:
print(f"{argc} arguments:")
for i in range(1, argc + 1):
print(f"{i}: {argv[i]}")
