def minnumber(A):
    
    left=0
    right=len(A)-1

    if len(A)==0:
        return(-1)

    if len(A)==1:
        return(A[0])
    
    if A[left]<A[right]:
        return(0)
    
    while left<right:
        mid=(left+right)//2
        
        if A[right]<A[mid]:
             left=mid+1
        else:
             right=mid

    return left

             
def binarysearch(A,t,left,right):
    while left<=right:
        mid=(left + right)//2
        if A[mid]==t:
            return mid
        elif A[mid]<t:
            left=mid+1
        else:
            right=mid-1
    return -1



A=[4,5,6,7,0,2,3]
minn=minnumber(A)

t=6
leftarray=binarysearch(A,t,0,minn-1)
rightarray=binarysearch(A,t,minn,len(A)-1)

m=max(leftarray,rightarray)
print("at index : ",m)