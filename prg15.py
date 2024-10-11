n=int(input("Enter the number="))
c=0
while(n>0):
    digit=n%10
    if(digit==0):
        c=c+1
        break
    n=n//10
if(c==1):
    print("The given number is duck number")
else:
    print("The given number is not a duck number")
    
