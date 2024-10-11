def binary_search(st,en,li,k):
    for i in li:
        mid=(st+en)//2
        if li[mid]==k:
            return mid
        elif li[mid]>k:
            return binary_search(st,mid,li,k)
        else:
            return binary_search(mid+1,en,li,k)
    else:
        return -1

li=[7,9,4,6,3,2,8]
print(li)
n=len(li)
li.sort()
print("sorted list:",li)
k=int(input("enter the number to be searches:"))
print(k, "at index",binary_search(0,n-1,li,k))
