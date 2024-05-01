# lst = [1, 2, 3, 4, 5]
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst = [10, 12, 30]
lst = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]

# Method 1
lst1 = lst.copy()
result = [(lst1[i]+(lst1[i+1]))/2 for i in range(len(lst1)-1) if i != lst1[-1]]
for item in result:
    lst1.insert(result.index(item)*2+1, item)
print(lst1)

