def duplicates(s):
    return "".join(dict.fromkeys(s))

print(duplicates("programming"))