s = input()
def makeint(m):
    try:
        m = int(m)
    except ValueError:
        m = 0
    return m
print(makeint(s))