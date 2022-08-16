def isIsomorphic(s,t):
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            if t[i] not in list(d.values()):
                d[s[i]] = t[i]
            else:
                return False
    temp = s
    s = ""
    for char in temp:
        s += d[char]

    if s == t:
        return True
    return False

isIsomorphic("abc","pqr")