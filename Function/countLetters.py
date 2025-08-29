def cntletter(s):
    lower = 0
    upper = 0
    for c in s:
        if c.islower():
            lower+=1
        elif c.isupper():
            upper+=1
    return lower, upper

print(cntletter("Hello World"))