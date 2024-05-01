lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# lst = [2, 9, 9, 2, 1, 1, 9, 9, 9]
# lst = [2, 1, 1, 2, 1, 1, 9, 1, 1]
min_value = 3
max_value = 6


for x in lst:
    condition = [x for x in lst if min_value <= x <= max_value]

    prod = 1
    for i in condition:
        prod *= i

if condition:
    print(f'Sum_: {sum(condition)}; Product: {prod}; List is: {list(condition)}')
else:
    print(f'List: {list(condition)} - list is None')








