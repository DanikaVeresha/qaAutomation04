
triangle = int(input('Enter size of triangle: '))

for item in range(triangle):
    symbol = '*'
    for j in range(triangle-1, -1, -1):
        if j > item:
            print(" ", end="")
        else:
            print(symbol, end="")
    print()
