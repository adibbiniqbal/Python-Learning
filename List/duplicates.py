lst = input('Enter numbers: ').split()
lst2 = []
for x in lst:
    if x not in lst2:
        lst2.append(x)
print(lst2)