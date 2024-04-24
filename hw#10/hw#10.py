
word = input('Enter word:')
reversed_word = word[::-1]

comparison_result = ((reversed_word.lower().strip() == word.lower().strip()) or
                     (reversed_word.upper().strip() == word.upper().strip()) or
                     (reversed_word.swapcase().strip() == word.swapcase().strip()) or
                     (reversed_word.casefold().strip() == word.casefold().strip()))

if comparison_result:
    print(f'Comparison result: {comparison_result}')
else:
    print(f'Comparison result: {comparison_result}')





