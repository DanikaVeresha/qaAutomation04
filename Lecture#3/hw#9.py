

n = int(input("Enter value 'n': "))
for j in range(1, n+1):
    print(' ' * 2 * (n-j), end='')
    for i in range(1, 2 * j):
        print(i if i <= j else 2 * j-i, end='')
        if i < 2 * j - 1:
            print(' ', end='')
    print()