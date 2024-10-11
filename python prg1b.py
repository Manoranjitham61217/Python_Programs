def liuguy(li):
    c=0
    for i in li:
        if (i%2==0) and (li[i]%2==0):
            c=c+1
            
        elif (i%2!=0) and (li[i]%2!=0):
            c=c+1
        
                 
    if c== len (li):
        print (" True")
    else:
        print (" False") 

    
li= []
n=int (input ("no of values:"))
for j in range (0, n+1):
    li. append(int (input ("enter the value:")))
liuguy (li)


