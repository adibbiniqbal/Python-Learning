num = int(input('enter number: '))
bin = ''
while num > 0:
    r = num%2
    bin = str(r) + bin
    num //= 2
print(bin)