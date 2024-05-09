import json
lst2dict = ([0, 1, 2, 3])
# lst2dict = (['a', 'A', 'b', 'B', 'c'])
# lst2dict = (['a', None, 'C'])
# lst2dict = ([])
# lst2dict = None


# def list2dict(lst):
#     if len(lst) % 2 != 0:
#         lst.pop()
#         result = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     else:
#         result = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return result

def list2dict(lst):
    if len(lst) % 2 != 0:
        lst.pop()
        result = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    else:
        return None
    return result


print(f'List: {lst2dict}; Type: {type(lst2dict)}')
print(f'Result: {list2dict(lst2dict)}; Type: {type(list2dict(lst2dict))}')



