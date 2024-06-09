"""Task 38."""
import time


def cache(func):
    cache_dict = {}
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        start = time.perf_counter_ns()
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        end = time.perf_counter_ns()
        return f'Result function "{func.__name__}"; Arguments: {key} -> {cache_dict[key]}\n' \
               f'Function "{func.__name__}" was called {calls} times\n' \
               f'Function "{func.__name__}" executed in {end - start} nano-seconds\n' \

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


print(add(1, 2))
print(add(x=1, y=2))
print(add(y=2, x=1))
print(sub(3, 4))
print(sub(x=3, y=4))
print(sub(y=4, x=3))
print(mul(5, 6))
print(mul(x=5, y=6))
print(mul(y=6, x=5))
print(div(7, 8))
print(div(x=7, y=8))
print(div(y=8, x=7))
