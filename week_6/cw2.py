s1 = "abceedg"
s2 = "ebc"

n = len(s2)
is_substr = False
for i in range(len(s1) - len(s2) + 1):
    if s1[i : i + n] == s2:
        is_substr = True
        break

print(is_substr)