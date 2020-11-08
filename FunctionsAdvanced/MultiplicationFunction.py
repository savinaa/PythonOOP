import functools
def multiply(*args):
    return functools.reduce(lambda a, b: a * b, args)