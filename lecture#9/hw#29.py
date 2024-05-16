
def linearize_list(lst):
    result = []
    for i in lst:
        if type(i) is list:
            result += linearize_list(i)
        else:
            result.append(i)
    return result


lst_obj = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
# lst_obj = [1, 2, [3, [4, 5, [6, 7]]], 8, 9, [10, [11, 12]], 13, [14, 15, [16, 17, [18, 19, [20, 21]]]]]
# lst_obj = ['a', 'b', ['c', 'c', [1, 2], 'z'], 'z', [5, ['y']], 'i']
# lst_obj = ['a', 'b', ['c', 'c', ['d', 'e'], 'z'], 'z', ['v', ['y']], 'i']

print(linearize_list(lst_obj))
