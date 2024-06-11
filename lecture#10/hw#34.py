"""Task 34."""


def custom_zip(*args, full=False, default=None):
    if full:
        max_len = max(len(arg) for arg in args)
        res = []
        for i in range(max_len):
            res.append(tuple(arg[i] if i < len(arg) else default for arg in args))
        return res
    else:
        return [tuple(arg[i] for arg in args) for i in range(min(len(arg) for arg in args))]


# lst = [1, 3, 5, 7, 8, 9, 10, 11]
# lst2 = [2, 4, 6]
lst = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8, 9, 10, 11]
print(custom_zip(lst, lst2))
print(type(custom_zip(lst, lst2)))
print('----------------------------')
print(custom_zip(lst, lst2, full=True, default="X"))
print(type(custom_zip(lst, lst2, full=True, default="X")))

