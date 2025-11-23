#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for ch in roman_string[::-1]:  # sondan başlayırıq
        value = roman_values.get(ch, 0)
        if value >= prev:
            total += value
        else:
            total -= value
        prev = value

    return total
