a=[8,5,3,9,6,2]
n=len(a)


for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            
print(a)




      
