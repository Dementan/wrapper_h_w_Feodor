def debug(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, res)
        func()
        return wrapper()


def mult(a, b):
    return a*b

# @debug
# print(mult(2, 3))
print(debug(mult(2,4)))

