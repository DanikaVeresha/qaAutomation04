
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
    result = sum(args, **kwargs) == 5
    @skip_if(result, f'becouse sum entered values is equal to 5 so condition is met.')
    def test_func(*args, **kwargs):
        assert result, (f'The expected sum of the values entered should be 5, but we '
                        f'got {sum(args, **kwargs)}')

    test_func(*args, **kwargs)


test_skip_if(1, 1, 3)




