
def dec(if_, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if if_:
                return f'Skipping test "{func.__name__}". Reason: {reason}'
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@dec(sum([10, 15]) == 25, 'becouse sum entered values is equal to 25 and so condition is met.')
def test_func(*args, **kwargs):
    return sum(args, **kwargs) == 25


print(test_func())
