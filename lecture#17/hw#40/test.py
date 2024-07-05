
def f():
    a = 7
    b = 10
    return a + b, 'Hello, World!'


def f1():
    a = 7
    b = 10
    return a + b, 'Hello, World!'


def delete_function(func):
    if func.__name__ == 'f':
        del func
    return 'Function has been deleted!'


print(f())
print(f1())
print(delete_function(print(f())))
