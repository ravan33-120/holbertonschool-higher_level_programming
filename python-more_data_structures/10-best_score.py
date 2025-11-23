#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    for key in a_dictionary:
        if best is None or a_dictionary[key] > a_dictionary[best]:
            best = key
    return best
