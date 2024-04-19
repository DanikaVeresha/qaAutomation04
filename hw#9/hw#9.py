
number = int(input('Enter value: '))

m = (2 * number) - 2
for i in range(0, number):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print(i, end=' ')
    print(" ")
