def sortarray(A):
    b=len(A) 
    k=0
    while k<b:
        t=k+1
        while t<b:
            if A[k]>A[t]:
                temp=A[t]
                A[t]=A[k]
                A[k]=temp
            
            t+=1
        k+=1    
    print(A)
    return(A)


def chocolate(N,m):
    l=len(N)
    i=0
    int_min=0
    
    while i+m-1<l:
        int_dif=N[i+m-1]-N[i]
        if i==0:
            int_min=int_dif
        if int_dif < int_min:
            int_min=int_dif
            print(int_min)
        i+=1

    print("minimum chocolate distributed are : ",int_min)

A=[7, 3, 2, 4, 9, 12, 5]
m=3
print(A)
N=sortarray(A)
print(N)
chocolate(N,m)