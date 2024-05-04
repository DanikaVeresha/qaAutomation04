users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19},
    {'name': 'Bob Anderwood',
     'age': 56},
    {'name': 'Anny Winchester',
     'age': 15},
]

# Method
result = [user['name'] for user in users if user['age'] >= 18]
print(f'Result: {result}')
