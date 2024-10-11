num= int(input("Enter the number"))
count=1
n=2
while(count<=num):
    for i in range(2,n):
        if(n%i==0):
            break
        else:
            print(n)
            count=count+1
            n=n+1
        