import math

# second_largest_number = ([])  # None
# second_largest_number = ([1, 1])  # None
# second_largest_number = ([1, 2, 3, 4, 5])  # 4
# second_largest_number = ([-1, -2, -3, -4, -5]) # -2
# second_largest_number = [-2, -5, -6] # -5
second_largest_number = ([0, 0, 0, 0, 0, 0]) # None


def second_largest_number_(lst):
    if len(lst) == 0:
        return None
    print(f'List`s len: {len(lst)}')
    max_number = -math.inf
    second_max_number = -math.inf
    for i in lst:
        if i > max_number:
            second_max_number = max_number
            max_number = i
        elif i > second_max_number and i != max_number:
            second_max_number = i
    if second_max_number == -math.inf:
        return None
    return second_max_number


print(second_largest_number_(second_largest_number))
