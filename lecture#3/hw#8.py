"""Task 8."""


print('To test this file, read the teachers requirements \n'
      'at the link: https://lms.ithillel.ua/groups/65b95f9a581cb89d38bea262/homeworks/66213c710eb47a7edbd54707')
min_width = int(input('Enter minimal width: '))
max_width = int(input('Enter maximal width: '))

if min_width > max_width:
    print('Error: Sorry, your values min_width and max_width of the diamond pattern incorrect. \n'
          'Please enter correct values min_width and max_width and try again!')
elif (max_width - min_width) % 2 != 0:
    print('Error: Sorry, your values min_width and max_width of the diamond pattern incorrect. \n'
          'Please enter the correct min_width and max_width values so that the difference between \n'
          'these values is a multiple of 2 and try again!')
else:
    for row in range(min_width, max_width+2, 2):
        if row == min_width:
            row = ' ' * ((max_width-row) // 2) + "*" * min_width
            print(row)
        else:
            print(' ' * ((max_width-row) // 2) + "*" + ' '*(row-2) + "*")
    for row in range(max_width-2, min_width-2, -2):
        if row > min_width:
            row = ' ' * ((max_width-row) // 2) + '*' + ' '*(row-2) + "*"
            print(row)
        else:
            print(' ' * ((max_width-row) // 2) + "*" * min_width)



