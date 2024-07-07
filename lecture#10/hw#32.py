"""Task 32. Random string"""


import random


def random_string(length):
    """Generates a random string of the specified length"""
    res = (
        "".join(chr(random.randint(48, 57)) for _ in range(length)) +
        "".join(chr(random.randint(65, 90)) for _ in range(length)) +
        "".join(chr(random.randint(97, 122)) for _ in range(length))

    )
    return "".join(random.sample(res, length))


print(f'Random string: {random_string(10)}')
# print(type(random_string(10)))





