"""Task 29. List linea_rization"""


def linearize_list(lst):
    result = []
    for i in lst:
        if type(i) is list:
            result += linearize_list(i)
        else:
            result.append(i)
    return result


def linearize_list_v2(lst, is_first_call=True):
    if is_first_call:
        global result_v2
        result_v2 = []
    for i in lst:
        if type(i) is list:
            linearize_list_v2(i, False)
        else:
            result_v2.append(i)
    return result_v2


def linearize_list_v3(lst):
    result_v3 = []
    for i in lst:
        if isinstance(i, list):
            result_v3 += linearize_list(i)
        else:
            result_v3.append(i)
    return result_v3


lst_obj = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
# lst_obj = [1, 2, [3, [4, 5, [6, 7]]], 8, 9, [10, [11, 12]], 13, [14, 15, [16, 17, [18, 19, [20, 21]]]]]
# lst_obj = ['a', 'b', ['c', 'c', [1, 2], 'z'], 'z', [5, ['y']], 'i']
# lst_obj = ['a', 'b', ['c', 'c', ['d', 'e'], 'z'], 'z', ['v', ['y']], 'i']

print(linearize_list(lst_obj))
print(linearize_list_v2(lst_obj))
print(linearize_list_v3(lst_obj))




