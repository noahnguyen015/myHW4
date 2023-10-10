def allcaps(func):
    def wrapper():
        s = func()
        s = s.upper()
        print(s)
    return wrapper