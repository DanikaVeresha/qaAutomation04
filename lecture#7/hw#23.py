# second_largest_number = ([])  # None
# second_largest_number = ([1, 1])  # None
# second_largest_number = ([1, 2, 3, 4, 5])  # 4
# second_largest_number = ([-1, -2, -3, -4, -5])
second_largest_number = ([0, 0, 0, 0, 0, 0])


def second_largest_number_(lst):
    max_number = 0
    second_max_number = 0
    for i in lst:
        if i > max_number or i < max_number:
            second_max_number = max_number
            max_number = i
        elif i > second_max_number and i != max_number:
            second_max_number = i
    if second_max_number == 0 or len(lst) == 0:
        return None
    return second_max_number


print(second_largest_number_(second_largest_number))