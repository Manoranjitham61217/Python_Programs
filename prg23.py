li=[2,3,4,5,6,8,10,9]
def find(li,n):
    for i in li:
        if n==i:
            return li.index(i)
    return-1
print(find(li,9))
