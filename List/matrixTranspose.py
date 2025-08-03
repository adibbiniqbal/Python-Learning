mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = []
for i in range(len(mat)):
    c =[]
    for j in range(len(mat[0])):
        c.append(mat[j][i])
    s.append(c)
print(s)