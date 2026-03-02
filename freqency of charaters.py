def frequency(s):
    fre ={}
    for char in s:
        fre[char] = fre.get(char,0)+1

    return fre
print(frequency("Programminng"))