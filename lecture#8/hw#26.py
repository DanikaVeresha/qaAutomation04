"""Task 26. My decorator`s version"""


import time
from datetime import datetime


# def call_counter(path):
#
#     def inner(func):
#         func.calls = 0
#
#         def wrapper(*args):
#             start_time = datetime.now()
#             func(*args)
#             func.calls += 1
#             with open(path, 'a') as file:
#                 file.write(f'Function "{func.__name__}". Information below:\n'
#                            f'Was called {func.calls} times\n'
#                            f'Args: {args}\n'
#                            f'Return: {func.__doc__}\n'
#                            f'Function start time: {datetime.now()}\n'
#                            f'Function execution time: {datetime.now() - start_time}\n\n')
#             return func(*args)
#         return wrapper
#     return inner


"""Task 26. Correct decorator`s version"""


def call_counter(path):

    def inner(func):
        func.calls = 0

        def wrapper(*args):
            start_time = time.perf_counter()
            func(*args)
            func.calls += 1
            with open(path, 'a') as file:
                file.write(f'Function "{func.__name__}". Information below:\n'
                           f'Was called {func.calls} times\n'
                           f'Args: {args}\n'
                           f'Return: {func.__doc__}\n'
                           f'Function start time: {datetime.now()}\n'
                           f'Function execution time: {time.perf_counter() - start_time}\n\n')
            return func(*args)
        return wrapper
    return inner


@call_counter('data.txt')
def sum_(a, b):
    """Sum of numbers"""
    return sum((a, b))


@call_counter('data.txt')
def mul_(a, b):
    """Multiplication of numbers"""
    return a * b


@call_counter('data.txt')
def div_(a, b):
    """Division of numbers"""
    return a / b


@call_counter('data.txt')
def sub_(a, b):
    """Subtraction of numbers"""
    return a - b


print(f'Sum: {sum_(1, 2)}')
print(f'Sum: {sum_(3, 4)}')
print(f'Mul: {mul_(2, 3)}')
print(f'Div: {div_(6, 3)}')
print(f'Div: {div_(6, 1)}')
print(f'Div: {div_(6, 2)}')
print(f'Sub: {sub_(6, 2)}')
print(f'Sub: {sub_(6, 1)}')

