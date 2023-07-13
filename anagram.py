def anagram(S,T):
    if len(S)!=len(T):
        return False
    
    dic={ }

    for char in S:
        if char not in dic:
            dic[char]=1
        else:
            dic[char]+=1
    
    for char in T:
        if char not in dic or dic[char]==0:
            return False
        else :
            dic[char]-=1
    
    return True

print(anagram("ccac","caac"))