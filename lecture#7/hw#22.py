
# lst2dict = ([0, 1, 2, 3])
lst2dict = (['a', 'A', 'b', 'B', 'c'])
# lst2dict = (['a', None, 'C'])
# lst2dict = ([])


def list2dict_(lst):
    test_lst = lst.copy()
    if len(test_lst) % 2 != 0:
        test_lst.pop()
    return {test_lst[i]: test_lst[i + 1] for i in range(0, len(test_lst), 2)}


# Output
print(f'List`s result after run of function: {list2dict_(lst2dict)}')
print(f'Source list: {lst2dict}')





