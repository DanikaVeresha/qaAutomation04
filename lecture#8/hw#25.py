

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
def test_sum():
    assert sum([1, 2, 3]) == 6


@skip_if(False)
def test_sum_():
    assert sum([2, 2, 3]) == 6, 'Expected 6'


test_sum()
test_sum_()