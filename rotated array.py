def rotate_array(A,p,l):
    B = [ ]
    i=0
    n=p
    while p<l:
        B.append(A[p])
        p+=1
        i+=1
    j=0
    while j<n:
        B.append(A[j])
        j+=1
    print(B)

def check_array(A,t,l):
    i=0
    while i<l:
        if A[i]==t:
            d=i
            break
        else :
            d=-1
        i+=1
    print("target : ",d)

A=[0,1,2,3,5,6,7]
t=3
p=3
l=len(A)
rotate_array(A,p,l)
check_array(A,t,l)