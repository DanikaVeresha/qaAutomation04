"""Task 38."""
import time


def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return wrapper


@cache
def add(x, y):
    return x + y


@cache
def sub(x, y):
    return x - y


@cache
def mul(x, y):
    return x * y


@cache
def div(x, y):
    return x / y


print('-----Sum-----')
print(add(1, 2))
print(add(x=1, y=2))
print(add(y=2, x=1))
print('-----Sub-----')
print(sub(3, 4))
print(sub(x=3, y=4))
print(sub(y=4, x=3))
print('-----Mul-----')
print(mul(5, 6))
print(mul(x=5, y=6))
print(mul(y=6, x=5))
print('-----Div-----')
print(div(7, 8))
print(div(x=7, y=8))
print(div(y=8, x=7))
print('-----Mul[sum*sub]-----')
print(add(3, 5) * sub(4, 2))
