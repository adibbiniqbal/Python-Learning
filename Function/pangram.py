def pangram(s):
    st = set()
    for c in s.lower():
        if c.isalpha():
            st.add(c)
    return len(st) == 26

print(pangram("The quick brown fox jumps over the lazy dog"))  
print(pangram("Hello World"))                                 