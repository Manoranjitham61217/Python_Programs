a,b,c,d=0,0,0,0
li=['!','@','#','$','%','^','&','*']
pw=input("Enter your password:")
if(len(pw)>=8):
    for i in pw:
        if(i.islower()):
            a+=1
        if(i.isupper()):
            b+=1
        if(i.isdigit()):
            c+=1
        if(i in li):
            d+=1
        else:
            print("valid and strong Password")

if(a>=1 and b>=1 and c>=1 and d>=1):
    print("valid password")
else:
    print("Invalid password")
