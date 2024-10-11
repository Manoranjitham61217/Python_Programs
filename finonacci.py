n=int(input())
a=0
b=1
c=a+b
#print("Fibonacci Series:")
#print(a,b,end=" ")
for i in range(2,n):
    #print(c,end=" ")
    a=b
    b=c
    c=a+b
print(c)
