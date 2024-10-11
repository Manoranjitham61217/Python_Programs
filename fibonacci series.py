a=1
b=1
n=int(input("Enter no of terms:"))
print(a)
print(b)
for i in range(1,n):
    c=a+b
    print(c)
    a=b
    b=c
