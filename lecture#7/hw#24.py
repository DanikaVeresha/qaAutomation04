dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan']

# Output
dates.sort(key=lambda x: int(x.split('-')[0] if x.split('-')[1] != 'Jan' else 0))
print(dates)

