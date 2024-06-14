"""Task 14."""

number_list = range(16)
print(list(number_list))    # List of numbers from 0 to 15

# Elements are divisible by 3 but not by 5
print(list(item for item in number_list if item % 3 == 0 and item % 5 != 0))

# Elements are divisible by 5 but not by 3
print(list(item for item in number_list if item % 5 == 0 and item % 3 != 0))

# Elements are divisible by 3 and 5
print(list(item for item in number_list if item % 3 == 0 and item % 5 == 0))

# Output:
print(list(item for item in range(16) if item % 3 == 0 and item % 5 != 0))
print(list(item for item in range(16) if item % 5 == 0 and item % 3 != 0))
print(list(item for item in range(16) if item % 3 == 0 and item % 5 == 0))
