n = int(input('enter number of numbers: '))
sumPos = 0
sumNeg = 0 
while(n>0):
    num = int(input('enter a number: '))
    if num > 0:
        sumPos += num
    else:
        sumNeg += num
    n-=1
print(sumPos)
print(sumNeg)