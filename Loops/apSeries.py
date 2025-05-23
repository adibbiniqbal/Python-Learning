a = int(input('enter starting term: '))
d = int(input('enter common difference: '))
n = int(input('enter n: '))
for i in range(1,n):
    a += d
print(f'nth term is {a}')
