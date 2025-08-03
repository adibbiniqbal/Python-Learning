l1 = input('Enter l1: ').split()
l2 = input('Enter l2: ').split()
ans = []
for x in l1:
    if x in l2:
        ans.append(int(x))
print(ans)