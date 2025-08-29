countries = {}
n = int(input('enter number of countries: '))
for i in range(n):
    c = input('enter country name: ')
    if c[0].upper() not in countries:
        countries[c[0].upper()] = [c]
    else:
        countries[c[0].upper()].append(c)
print(countries)
