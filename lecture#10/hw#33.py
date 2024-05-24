"""
Task 33.
Name: Custom map
"""


def custom_map(func, *args):
    return [func(*params) for params in zip(*args)]


print(f'Sum item in two lists: {custom_map(sum, [[1, 2, 3], [3, 5, 0, 5]])}')
print(f'Sum items from two lists: {custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0])}')
print(f'List`s lenght in lists list: {custom_map(len, [[], (2, 4), [1, 3, 5, 7]])}')
print('---------------------------')
print(f'Sum items from lists: {custom_map(lambda x, y, z: x + y + z, [1, 2, 3, 4], [3, 5, 0], [1, 2, 3, 9])}')
print(f'Minimum value in each list of the main list: {custom_map(min, [[1, 2, 3, 4, 5], [1, 2, 3], [3, 5, 1, 5]])}')
print(f'Maximum value in each list of the main list: {custom_map(max, [[1, 2, 3, 4, 5], [1, 2, 3], [3, 5, 1, 5]])}')
print(f'Prod: {custom_map(lambda x, y, z: x * y * z, [1, 2, 3, 4], [3, 5, 0], [1, 2, 3, 9])}')
print(f'Division: {custom_map(lambda x, y, z: round(x / y / z, 2) if y != 0 and z !=0 else None, [1, 2, 3, 4], [3, 0, 1], [1, 2, 3, 9])}')
