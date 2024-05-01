lst = [1, 2, 3, 4, 5]
# Run each option separately since there is only one list !!!!

# # Training option 1
lst1 = lst.copy()
result = [(i+(i + 1))/2 for i in lst1 if i != 5]
lst1.insert(1, result[0])
lst1.insert(3, result[1])
lst1.insert(5, result[2])
lst1.insert(7, result[3])
print(lst1)

# Training option 2
lst2 = lst.copy()
result = [(i+(i + 1))/2 for i in lst2 if i != 5]
for item in result:
    lst2.insert(result.index(item)*2+1, item)
print(lst2)

# Training option 3
result = [(i+(i + 1))/2 for i in lst if i != 5]
main_result = []
for item in result:
    main_result.append(lst[result.index(item)])
    main_result.append(item)
main_result.append(5)
print(main_result)

