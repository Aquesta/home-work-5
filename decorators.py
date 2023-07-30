def add_separators(f):
    def inner(*args, **kwargs):
        print('*'*100)
        result = f(*args, **kwargs)
        print('*'*100)
        return result
    return inner
