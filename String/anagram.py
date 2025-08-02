s1 = input('enter string 1: ')
s2 = input('enter string 2: ')
if sorted(s1) == sorted(s2):
    print('anagram')
else:
    print('not anagram')