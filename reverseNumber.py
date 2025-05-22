num = int(input('enter number: '))
reverse = 0
while num>0:
    digit = num%10
    num //= 10
    reverse = reverse*10 + digit
print(f'digits = {reverse}')
