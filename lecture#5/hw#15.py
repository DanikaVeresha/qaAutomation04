lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# lst = [2, 9, 9, 2, 1, 1, 9, 9, 9]
min_value = 3
max_value = 6


condition = (x for x in lst if min_value <= x <= max_value)

if condition:
    print(f'Sum_: {sum(condition)}')

# and
condition_1 = (x for x in lst if min_value <= x <= max_value)
if condition_1:
    prod = 1
    for i in condition_1:
        prod *= i
    print(f'Product: {prod}')







