
def nxtpermutation(s):
    i = len(s) - 2
    while i >= 0 and s[i + 1] <= s[i]:
        i -= 1

    if i >= 0:
        j = len(s) - 1
        while s[j] <= s[i]:
            j -= 1
        (s[i], s[j]) = (s[j], s[i])

    s[::] = s[:i + 1] + s[i + 1:][::-1]
    print("first : ",s[:i+1],"second :", s[i+1:],"third : ",s[::-1],"fourth : ",s[i+1:][::-1])
    return(s)

A=[1,2,3]
print("/n",nxtpermutation(A))