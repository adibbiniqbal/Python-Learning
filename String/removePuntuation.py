str = input('enter a string: ')
punctuations = '''!"()\-[]{};:'"\,<>./?@#$%^&*_~'''
ans = ''
for x in str:
    if x not in punctuations:
        ans += x
print(ans)