users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19}
]

# Method
result = [user['name'] for user in users if user['age'] >= 18]
print(f'Result: {result}')
