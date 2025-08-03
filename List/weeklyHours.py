hours = input('Enter daily hours of the week: ').split()
ans = 0
for x in hours:
    ans += int(x)
print(ans)