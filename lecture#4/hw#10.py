"""Task 10."""


word = input('Enter word:').casefold().strip()
reversed_word = word[::-1]

comparison_result = (reversed_word == word)

if comparison_result:
    print(f'Comparison result var1: {comparison_result}')
else:
    print(f'Comparison result var1: {comparison_result}')

# or var2
result = ''.join(reversed(word))
print(f'Comparison result var2: {result == word}')


# or var3
for i, j in enumerate(word):
    if j != word[-i - 1]:
        print(f'Comparison result var3: False')
    else:
        print(f'Comparison result var3: True')