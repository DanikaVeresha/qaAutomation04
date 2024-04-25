sentences = "Hello all. Here`s pretty cold and hot. Choose yourself"
arr = sentences.split('.')
print(arr)
result = []
for i in arr:
    result += str(len(i.split()))
print(f'[{", ".join(result)}]')











