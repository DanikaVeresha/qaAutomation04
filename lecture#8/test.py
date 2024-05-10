
def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f'Skipping test "{func.__name__}". Reason: {reason}')
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator


@skip_if(True, 'This test is skipped')
def f1(*args, **kwargs):
    assert sum(args, **kwargs) == 5


@skip_if(False)
def f1(*args, **kwargs):
    assert sum(args, **kwargs) == 5, f'Expected 5, but got {sum(args, **kwargs)}'


f1(2, 3)

