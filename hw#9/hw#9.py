

n = int(input("Enter a number: "))
for j in range(1, n+1):
    print(' '*(3*(n-j)), end='')
    for i in range(1, 2*j):
        print(f'{i:2}' if i <=j else f'{2*j-i:2}', end='')
        if i<2*j-1:
            print(' ', end='')
    print()