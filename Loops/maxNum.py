n = int(input('enter number of numbers: '))
max = -2**31
while(n>0):
    num = int(input('enter a number: '))
    if num > max:
        max = num
    n-=1
print(max)