
def generator(lst: list, iter_num: int = None):
    while iter_num is None:
        for i_lst in range(len(lst)):
            yield lst[i_lst]
    else:
        for i_len in range(iter_num):
            for item_lst in range(len(lst)):
                yield lst[item_lst]


lst_obj = ['a', 'b', 'c']
for item in generator(lst_obj, 3):
    print(item)
