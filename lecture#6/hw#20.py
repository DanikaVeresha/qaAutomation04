
# with open('hw#20.txt', 'x') as f:
# Спочатку я виконала такий варіант, для створення даного файлу та запису в нього нищевказаних даних!

with open('hw#20.txt', 'w') as f:
    f.writelines(['Hello\n', 'Hello,World\n', 'desh288diesh@gmail.com\n',
                  'Danika\n', 'DESH288DIESH@GMAIL.COM\n', 'DESH288DIESH@GMAIL.ccc\n'])

print('------------TextFile---------------')
with open('hw#20.txt', 'r') as x:
    data = x.read()
    print(data)
    print('----------Last Max Word------------')
    list_words = list(data.split())
    MAX = list_words[0]
    MIN = list_words[0]
    for i in list_words:
        if len(i) >= len(MAX):
            MAX = i
    print(f'The last word in the file with the maximum lengthh: {MAX} - Word lenght: {len(MAX)} symbols')


