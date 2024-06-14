"""Task 17."""


arr = [['a', 'c', 'e'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]


# Method
print('------Source arry below-----------')
for i in arr:
    print(i)
print('------Result(sort for columns) below----------------')
result = [[sorted(arr, key=lambda x: x[j])[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
output = [[result[i][j] for i in range(len(result))] for j in range(len(result[0]))]
for item in output:
    print(item)














