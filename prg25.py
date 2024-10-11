def BinarySearch(s,e,li,se):#Function Definition
    mid=(s+e)//2
    if li[mid]==se:
        return mid
    elif li[mid]>se:
        return BinarySearch(s,mid,li,se)
    elif li[mid]<se:
        return BinarySearch(mid+1,e,li,se)
li=[]
n=int(input("Enter the value N:"))

for i in range(n):
    li.append(int(input("Enter the value for list:")))

li.sort()
se=int(input("Enter the search element:"))
print('Index', format(se) ,'is',BinarySearch(0,n-1,li,se))
                            
