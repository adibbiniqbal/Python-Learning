def max3(a,b,c):
    if a > b:
        return a if a > c else c
    else:
        return b if b > c else c

print(max3(1,2,3))