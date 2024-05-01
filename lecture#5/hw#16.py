# lst = [1, 2, 3, 4, 5]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Run each option separately since there is only one list !!!!


# Training option 1
lst2 = lst.copy()
result = [(i+(i + 1))/2 for i in lst2 if i != lst2[-1]]
for item in result:
    lst2.insert(result.index(item)*2+1, item)
print(lst2)

# Training option 2
result = [(i+(i + 1))/2 for i in lst if i != lst[-1]]
main_result = []
for item in result:
    main_result.append(lst[result.index(item)])
    main_result.append(item)
main_result.append(lst[-1])
print(main_result)

