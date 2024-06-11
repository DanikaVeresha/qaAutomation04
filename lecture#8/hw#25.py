"""Task 25."""


def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f'Skipping test "{func.__name__}". Reason: {reason}')
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


values = [10, 5, 5]
if_ = 25


@skip_if(condition=sum(values) == if_,
         reason=f'becouse sum entered values is equal to {sum(values)} and so condition is met.')
def test_func(values):
    result = sum(values)
    return f'{result == if_}'


print(test_func(values))




