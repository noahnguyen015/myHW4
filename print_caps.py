def allcaps(func):
    def wrapper():
        s = func()
        s = s.upper()
        print(f'{s}')
    return wrapper