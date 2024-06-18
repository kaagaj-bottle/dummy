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
    count = 0
    for ch in text:
        if ch != " ":
            count += 1
    return count
