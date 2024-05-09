
# lst2dict = ([0, 1, 2, 3])
lst2dict = (['a', 'A', 'b', 'B', 'c'])
# lst2dict = (['a', None, 'C'])
# lst2dict = ([])


def list2dict_(lst):
    if len(lst) % 2 != 0:
        lst.pop()
    return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}


# Output
print(list2dict_(lst2dict))





