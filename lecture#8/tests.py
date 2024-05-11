

def dec(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs):
            return ('Reason: The test is skipped because the condition is met, '
                    'the sum of the entered values is equal to the specified condition')
        else:
            return func(*args, **kwargs)
    return wrapper

@dec
def func(*args, **kwargs):
    result = sum(args, **kwargs) == 10
    return result


print(func(10, 0))
