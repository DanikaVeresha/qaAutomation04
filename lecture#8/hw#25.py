
def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition == True:
                print(f'Skipping test "{func.__name__}". Reason: {reason}')
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator


a = 2
b = 4
result = sum([a, b]) == 5


@skip_if(result, f'Condition met. We got {result}, because {a} + {b} = {a + b}')
def func_():
    assert result, f'Expected 5, but got {result} because {a} + {b} = {a + b}'


func_()
