def palindrome(s):
    s1 = s.lower().replace(" ","")
    return  s == s1[::-1]

print(palindrome("subash"))

