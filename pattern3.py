rows=int(input())
for i in range(rows):
    if i%2==0:
        if i==4:
            print("*")
        else:
            print("*"*5)
    else:
        print("*")

