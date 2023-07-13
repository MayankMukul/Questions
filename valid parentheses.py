def isvalidp(S):

    stack=[]
    dict = {'(':')','{':'}','[':']'}

    for char in S :
        if char in dict:
            stack.append(char)
        elif not stack or dict[stack.pop()] != char:
            return False


    if len(stack)==0:
        return True       
    

S="()[]"
print(isvalidp(S))