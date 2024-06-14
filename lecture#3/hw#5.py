"""Task 5."""


value_a = int(input('Enter "a": '))
value_b = int(input('Enter "b": '))
value_c = int(input('Enter "c": '))

if value_a > value_b and value_a > value_c:
    print(f'Max_value "a": {value_a}')
elif value_b > value_a and value_b > value_c:
    print(f'Max_value "b": {value_b}')
else:
    print(f'Max_value "c": {value_c}')
