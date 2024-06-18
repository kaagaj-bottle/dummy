def sum(arg):
    s = 0
    for val in arg:
        s += val

    return s


def multiply(arg):
    p = 1
    for val in arg:
        p *= val
    return p


def count_char(text):
    countMap = {}

    for ch in text:
        countMap[ch] = countMap.get(ch, 0) + 1

    return countMap
