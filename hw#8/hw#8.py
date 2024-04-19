min_width_v1 = 3
max_width_v1 = 5
min_width_v2 = 1
max_width_v2 = 3
min_width_v3 = 2
max_width_v3 = 6
min_width_v4 = 3
max_width_v4 = 9


while True:
    print('To test this file, read the teachers requirements at the link: https://lms.ithillel.ua/groups/65b95f9a581cb89d38bea262/homeworks/66213c710eb47a7edbd54707')
    min_width = int(input('Enter minimal width: '))
    max_width = int(input('Enter maximal width: '))

    res = max_width / min_width

    if min_width > max_width:
        print('Error: Sorry, your values min_width and max_width of the diamond pattern incorrect. \n'
              'Please enter correct values min_width and max_width and try again!')
    elif res % 2 == 0:
        print('Error: Sorry, your values min_width and max_width of the diamond pattern incorrect. \n'
              'Please enter the correct min_width and max_width values so that the difference between \n'
              'these values is a multiple of 2 and try again!')
    else:
        if min_width == min_width_v1 and max_width == max_width_v1:
            for i in range(min_width, max_width, 2):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)
            for i in range(max_width, min_width, -2):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i[0], (' ' * 1), i[-1])
            for i in range(min_width, max_width, 2):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)

        elif min_width == min_width_v2 and max_width == max_width_v2:
            for i in range(min_width, max_width, 2):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)
            for i in range(max_width, min_width, -2):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i[0], i[-1])
            for i in range(min_width, max_width, 2):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)

        elif min_width == min_width_v3 and max_width == max_width_v3:
            for i in range(min_width, max_width, 4):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)
            for i in range(max_width, min_width, -4):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print('', i[0], '', i[-1])
            for i in range(max_width, min_width, -4):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i[0], '', ' ', i[-1])
            for i in range(max_width, min_width, -4):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print('', i[0], '', i[-1])
            for i in range(min_width, max_width, 4):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)

        elif min_width == min_width_v4 and max_width == max_width_v4:
            for i in range(min_width, max_width, 6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)
            for i in range(max_width, min_width, -6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(' ', i[0], ' ', i[-1])
            for i in range(max_width, min_width, -6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print('', i[0], ' ', ' ', i[-1])
            for i in range(max_width, min_width, -6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i[0], ' ',' ',' ',  i[-1])
            for i in range(max_width, min_width, -6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print('', i[0], ' ', ' ', i[-1])
            for i in range(max_width, min_width, -6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(' ', i[0], ' ', i[-1])
            for i in range(min_width, max_width, 6):
                i = ' ' * ((max_width - i) // 2) + '*' * i
                print(i)
        else:
            print('To test this file, enter the correct values for each block, according to the teacher’s\n'
                  ' requirements! You can view the requirements at the link: https://lms.ithillel.ua/groups/65b95f9a581cb89d38bea262/homeworks/66213c710eb47a7edbd54707')
            break