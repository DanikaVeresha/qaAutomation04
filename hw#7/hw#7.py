
triangle = int(input('Enter size of triangle: '))

a = triangle
for item in range(a):
    symbol = '*'
    for j in range(a-1, -1, -1):
        if j > item:
            print(" ", end="")
        else:
            print(symbol, end="")
            symbol *= 1
    print(' ')
