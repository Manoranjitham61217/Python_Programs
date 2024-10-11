def swap (a, b):
    temp=a
    a=b
    b=temp
    return a, b
               
a=int (input ("enter the value1:"))
b=int (input ("enter the value2:"))
print (swap (a, b))
