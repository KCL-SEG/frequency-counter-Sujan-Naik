"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def toString(item):
    if type(item) is not str:
        return str(item)
    return item

def frequencies(items):
    frequencies = {}
    # Your code goes here
    string_items = map(toString, items)
    for string_item in string_items:
        if frequencies.keys().__contains__(string_item):
            frequencies[string_item] += 1
        else:
            frequencies[string_item] = 1
    return frequencies
