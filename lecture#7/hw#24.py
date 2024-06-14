"""Task 24."""


# dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan']
dates = ['1-Dec', '12-Apr', '17-Apr', '31-Dec', '19-Jan', '4-Jan', '12-Dec']


def sortdates(dates):
    month_ = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = month_.index(dates.split('-')[1])
    day = int(dates.split('-')[0])
    return month, day


dates.sort(key=sortdates)
print(dates)


