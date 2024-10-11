def evenodd(lil):
    lil=[2,1,4,3,6,7,6,3]
    l=len(li)
    for i in range(l):
        if i%2==1 and lil[i]%2!=1:
            return false
        elif i%2==0 and lil[i]%2!=0:
            return false
    return true

