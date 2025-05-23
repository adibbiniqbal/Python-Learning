n = int(input('enter n: '))
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c 