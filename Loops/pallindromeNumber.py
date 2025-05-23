num = int(input('enter number: '))
numCopy = num
reverse = 0
while num>0:
    digit = num%10
    num //= 10
    reverse = reverse*10 + digit
print(numCopy==reverse)
