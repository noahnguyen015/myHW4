def allcaps(func):
    def wrapper():
        s = func()
        s = s.upper()
        return s
    return wrapper