n=int(input())
count=0
#count=len(str(n))
#print(count)
if n==0:
    print(1)
else:
    while n!=0:
        r=n%10
        count+=1
        n=n//10

    print(count)
    
