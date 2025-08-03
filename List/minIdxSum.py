fav1 = input('Enter fav1: ').split()
fav2 = input('Enter fav2: ').split()
minidx = 2**31
for x in fav1:
    if x in fav2:
        if fav1.index(x)+fav2.index(x) < minidx:
            minidx = fav1.index(x)+fav2.index(x)
            idx = fav1.index(x)
print(fav1[idx])