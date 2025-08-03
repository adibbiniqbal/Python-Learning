lst = input('Enter numbers: ').split()
num = 0
for x in lst:
    num = num*10 + int(x)
print(num)