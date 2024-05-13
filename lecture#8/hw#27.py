"""My version, but it`s not entirely correct"""
# def generator(lst: list, iter_num: int = None):
#     while iter_num is None:
#         for i_lst in range(len(lst)):
#             yield lst[i_lst]
#     else:
#         for i_len in range(iter_num):
#             for item_lst in range(len(lst)):
#                 yield lst[item_lst]


def generator(lst: list, iter_num: int = None):
    """Correct version of generator function"""
    while True:
        if iter_num is None:
            for i_lst in range(len(lst)):
                yield lst[i_lst]
        else:
            for _ in range(iter_num):
                for item_lst in lst:
                    yield item_lst
            break


lst_obj = ['a', 'b']
for item in generator(lst_obj, 4):
    print(item)
# """Iteration option when the iter_num is None"""
# for item in generator(lst_obj):
#     print(item)
