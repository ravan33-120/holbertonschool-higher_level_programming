#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Son rəqəmi tapırıq
last_digit = number % 10 if number >= 0 else -(-number % 10)

# Çap edirik
print(f"Last digit of {number} is {last_digit}", end=" ")

# Şərtə görə əlavə mesaj
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:  # last_digit < 6 və 0 deyil
    print("and is less than 6 and not 0")
