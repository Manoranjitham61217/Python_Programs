n=input("enter the number=")
sum=0
for i in n:
    sum+=int(i)**3
if sum==int(n):
    print("Armstrong")
else:
    print("not armstrong")
