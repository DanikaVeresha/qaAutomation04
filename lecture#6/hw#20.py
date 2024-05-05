
# with open('hw#20.txt', 'x') as f:
# Спочатку я виконала такий варіант, для створення даного файлу та запису в нього нищевказаних даних!

with open('hw#20.txt', 'w') as f:
    f.writelines(['Hello\n', 'Hello World\n', 'desh288diesh@gmail.com\n',
                  'Danika\n', 'DESH288DIESH@GMAIL.COM\n', 'DESH288DIESH@GMAIL.ccc\n'])

print('----------Last Max Word------------')
for item in open('hw#20.txt', 'r'):
    list_words = list(item)
    max_value = list_words[0]
    if len(item) >= len(max_value):
        max_value = item
print(f'The last string in the file with the maximum lengthh: {max_value}'
      f'String lenght: {len(max_value)} symbols\n'
      f'Type: {type(max_value)}')



