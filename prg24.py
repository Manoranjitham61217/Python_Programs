def add(a,b):
    return a+b
def difference(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
def floor_division(a,b):
    return a//b
def exponent(a,B):
    return a**b

a=float(input())
b=float(input())

ch=input("""Enter the choice
+-add
--difference
*-multiply
/-division
%-modulus
//-floor_division
**-exponent
""")
if(ch=="+"):
    print(add,(a,b))
elif(ch=="-"):
    print(difference(a,b))
elif(ch=="*"):
    print(multiply(a,b))
elif(ch=="/"):
    print(division(a,b))
elif(ch=="%"):
    print(modulus(a,b))
elif(ch=="//"):
    print(floor_division(a,b))
else:
    print(exponent(a,b))



