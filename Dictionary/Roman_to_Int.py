roman = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}
num = input('Enter roman number: ')
num = num.upper()
ans = 0
i = 0
while i < len(num):
    if i + 1 < len(num) and roman[num[i]] < roman[num[i+1]]:
        ans += roman[num[i+1]] - roman[num[i]]
        i+=2
    else:
        ans += roman[num[i]]
        i += 1
print(ans)    