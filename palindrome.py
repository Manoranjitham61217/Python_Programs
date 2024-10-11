def palindrome(a):
    a=str()
    b=a[::-1]
    if b==a:
        return True
    else:
        return False

str1=input("enter string:")
str2=str1[::-1]
if str2==str1:
    print("Palindrome")
else:
    print("not a palindrome")
palindrome(str1)
