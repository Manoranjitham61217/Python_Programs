n=int(input("enter the number="))
x=1
f=1
while(x<=n-1):
    if(n%x==0):
        f=0
        break
        x=x+1
if f==1:
    print("prime number")
else:
    print("not a prime number")
