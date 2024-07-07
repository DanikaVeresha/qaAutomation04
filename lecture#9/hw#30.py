"""Task 30. Time schedule"""


from datetime import timedelta, datetime


def time_schedule(date: str, time: str, total_lectures: int):
    """Version 1 of the solution: Generator Function that returns the time schedule lecture(my favorite version)"""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['Jany', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    date = datetime.strptime(date, '%d%m%Y')
    time = datetime.strptime(time, '%H%M')
    if date.strftime('%A') == 'Thursday':
        for number in range(1, total_lectures + 1):
            yield (f'Lecture {number:>2}: {date.strftime("%d")} {months[date.month - 1]} '
                   f'{date.year} {time.strftime("%H:%M")}')
            if number % 2 != 0:
                date += timedelta(days=4)
            if number % 2 == 0:
                date += timedelta(days=3)

    elif date.strftime('%A') == 'Monday':
        for number in range(1, total_lectures + 1):
            yield (f'Lecture {number:>2}: {date.strftime("%d")} {months[date.month - 1]} '
                   f'{date.year} {time.strftime("%H:%M")}')
            if number % 2 != 0:
                date += timedelta(days=3)
            if number % 2 == 0:
                date += timedelta(days=4)

    else:
        yield 'Sorry, there are no lectures on this day.'


# res = time_schedule('11042024', '1915', 32)
# print(res.__sizeof__()) # 320 bytes
# print(time_schedule('11042024', '1915', 32))
for item in time_schedule('11042024', '1915', 32):
    print(item)


print('-----------------Version 2 of the solution-----------------------')
start_lectures_date = '11042024'
time_start_lecture = '1915'
total_lessons = 32

list_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list_months = ['Jany', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
date_ = datetime.strptime(start_lectures_date, '%d%m%Y')
time_ = datetime.strptime(time_start_lecture, '%H%M')
if date_.strftime('%A') == 'Thursday':
    for i in range(1, total_lessons + 1):
        print(f'Lecture {i:>2}: {date_.strftime("%d")} {list_months[date_.month - 1]} '
              f'{date_.year} {time_.strftime("%H:%M")}')
        if i % 2 != 0:
            date_ += timedelta(days=4)
        if i % 2 == 0:
            date_ += timedelta(days=3)

elif date_.strftime('%A') == 'Monday':
    for i in range(1, total_lessons + 1):
        print(f'Lecture {i:>2}: {date_.strftime("%d")} {list_months[date_.month - 1]} '
              f'{date_.year} {time_.strftime("%H:%M")}')
        if i % 2 != 0:
            date_ += timedelta(days=3)
        if i % 2 == 0:
            date_ += timedelta(days=4)
else:
    print('Sorry, there are no lectures on this day.')


