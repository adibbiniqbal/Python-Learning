num = int(input('enter number: '))
cnt = 0
while num>0:
    num //= 10
    cnt += 1
print(f'digits = {cnt}')
