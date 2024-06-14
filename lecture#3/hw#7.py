"""Task 7. """

triangle = int(input('Enter size of triangle: '))
symbol = '*'

for item in range(triangle):
    for j in range(triangle-1, -1, -1):
        if j > item:
            print(" ", end="")
        else:
            print(symbol, end="")
    print()
