import json

lst2dict = ([0, 1, 2, 3])
lst2dict1 = (['a', 'A', 'b', 'B', 'c', 'C', 'g'])

print(f'List: {lst2dict}; Type: {type(lst2dict)}\n'
      f'List: {lst2dict1}; Type: {type(lst2dict1)}\n'
      f'-----------------without using json-------------------------')


# Function to convert list to dictionary without using json
def list2dict(lst):
    if len(lst) % 2 != 0:
        lst.pop()
        return {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    else:
        return {lst[i]: lst[i+1] for i in range(0, len(lst), 2)}


print(f'Result: {list2dict(lst2dict)}; Type: {type(list2dict(lst2dict))}\n'
      f'Result: {list2dict(lst2dict1)}; Type: {type(list2dict(lst2dict1))}\n'
      f'------------------using json------------------------')


# Function to convert list to dictionary using json
def list2dict_json(lst):
    if len(lst) % 2 != 0:
        lst.pop()
        res = json.dumps({lst[i]: lst[i + 1] for i in range(0, len(lst), 2)})
        return json.loads(res)
    else:
        res = json.dumps({lst[i]: lst[i+1] for i in range(0, len(lst), 2)})
        return json.loads(res)


print(f'Result: {list2dict_json(lst2dict)}; Type: {type(list2dict_json(lst2dict))}')
print(f'Result: {list2dict_json(lst2dict1)}; Type: {type(list2dict_json(lst2dict1))}')



