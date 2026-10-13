num = 12345


def rev(num):
    a = str(num)
    b = sorted(a, reverse = True)
    c = *b, sep = ""
    return c

rev(num)