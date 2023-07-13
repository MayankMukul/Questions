def checkduplicate(A):
    l=len(A)
    i=0
    b=0
    while i<l:       
        j=i+1
        while j<l:
            if A[i]==A[j]:
                b=1
                break
            j+=1
        i+=1 
    if b==1:
        print("true")
    elif b==0:
        print("false")
   

A=[1,1,1,3,3,4,3,2,4,2]
print(A)   
checkduplicate(A)