m1=int(input("Enter the mark 1="))
m2=int(input("Enter the mark 2="))
m3=int(input("Enter the mark 3="))
m4=int(input("Enter the mark 4="))
sum=m1+m2+m3+m4
avg=sum/4
if(90<=avg<100):
    print("Grade A+")
elif(80<=avg<90):
    print("Grade A")
elif(70<=avg<80):
    print("Grade B+")
elif(60<=avg<70):
    print("Grade B")
elif(50<=avg<60):
    print("Grade c")
else:
    print("Fail")
