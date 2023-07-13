def maxsubarray(A):
    l=len(A)
    maxnow = 0
    maxtotal= 0
    i=0
    while i < l :
        maxnow = maxnow + A[i]
        if maxtotal < maxnow  :
            maxtotal = maxnow
        if maxnow < 0 :
            maxnow = 0
        i+=1

    print('maximum of subarray : ',maxtotal,'\nmaxnow : ', maxnow) 

A=[1]
print(A)
maxsubarray(A)