s = input()
def makeint(m):
    try:
        m = int(m)
    except ValueError:
        m = 0
    finally:
        print('hello')
    return m * 5
print(makeint(s))