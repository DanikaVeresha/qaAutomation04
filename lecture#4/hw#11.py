"""Task 11."""


sentences = "Hello all. Here`s pretty cold and hot. Choose yourself"
arr = sentences.split('.')
print(f'Sentences: {arr}')
result = []
for i in arr:
    result += str(len(i.split()))
print(f'Result: [{", ".join(result)}]')












