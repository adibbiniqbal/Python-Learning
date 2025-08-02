str = input('Enter a string: ')
low, up = '', ''
for x in str:
    if x.islower():
        low += x
    elif x.isupper():
        up += x
print(low+up)