def invertDic(d):
    newd = {}
    for key, value in d.items():
        newd[value] = key
    return newd
    
d = {1:'A', 2: 'B', 3:'C'}
newd = invertDic(d)
print(newd)