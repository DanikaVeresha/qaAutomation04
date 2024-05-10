
def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f'Skipping test "{func.__name__}". Reason: {reason}')
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator


def test_skip_if(*args, **kwargs):
    num = 25
    result = sum(args, **kwargs) == num
    @skip_if(result, f'becouse sum entered values is equal to {num} so condition is met.')
    def test_func(*args, **kwargs):
        assert result, (f'The expected sum of the values entered should be {num}, but we '
                        f'got {sum(args, **kwargs)}')

    test_func(*args, **kwargs)


test_skip_if(10, 5, 10)




