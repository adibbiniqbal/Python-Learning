letters = input('Enter letters: ').split()
ans = []
for x in letters:
    if x not in ans:
        ans.append(x)
        cnt = 0
        for y in letters:
            if x==y:
                cnt += 1
        ans.append(cnt)
print(ans)
