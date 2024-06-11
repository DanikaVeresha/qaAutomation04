users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19},
    {'name': 'Bob Anderwood',
     'age': 11},
    {'name': 'Anny Winchester',
     'age': 15},
]

# Method
print(f'------Source data------')
for item in users:
    print(f'{item["name"]} - {item["age"]}')
result = [user['name'] for user in users if user['age'] >= 18]
print(f'--------Result---------\n'
      f'Result: {result}')
