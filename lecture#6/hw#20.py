"""Task 20."""


with open('hw#20.txt', 'w') as f:
    f.writelines(['line2\n', '\n', 'line3\n',
                  'line444444 444\n', 'line555555 555\n', 'line6\n'])
print('--------Result------------')
max_val = ''
for item in open('hw#20.txt', 'r'):
    if len(item) >= len(max_val):
        max_val = item
print(f'The last word in the file with the maximum lengthh: {max_val}')



