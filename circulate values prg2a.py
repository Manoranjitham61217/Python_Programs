li=int(input("enter the number of values:"))
for i in range(0,li+1):
    a=(input("enter the values:"))
    li=list(a)
   
n=int(input("Enter the number of times to circulate:"))
print(li(a[n:])+li(a[:n]))
