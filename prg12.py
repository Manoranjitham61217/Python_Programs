n=int(input("Enter the Number="))
sum=0
for j in range(1,n+1):
    for i in range(2,j):
        if(j%i==0):
            sum=sum+j
            break
        print(sum)
