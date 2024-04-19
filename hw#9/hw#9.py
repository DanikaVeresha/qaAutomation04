
number = int(input('Enter value: '))

if number >= 1 and number <= 9:
    k = (2 * number) - 2
    for i in range(0, number):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(number, end=' ')
        print(" ")
else:
    print('Error: Your values "n" invalid\n'
          'Please enter valid values "n" where 1 <= n <= 9')

