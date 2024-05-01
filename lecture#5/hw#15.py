lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]   # True
# lst = [2, 9, 9, 2, 1, 1, 9, 9, 9]
# lst = [2, 1, 1, 2, 1, 1, 9, 1, 1]
# lst = []
# lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]

MIN = 3
MAX = 6

# for item in lst:
check = [x for x in lst if MIN <= x <= MAX]
# product of all elements in the new list
value_0 = 1
for i in check:
    value_0 *= i

# checking the sum of all elements of the new list and their product
if check:
    print(f'Sum_: {sum(check)}; Product: {value_0}; '
          f'List is: {check}')
else:
    print(f'Sum_: {None}; Product: {None}; '
          f'List is: {check}')









