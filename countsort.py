def countsort(li):
    max1=max(li)
    cli=[0]*(max1+1)
    print(cli)
    for i in li:
        cli[i]+=1
    j=0
    print(cli)
    for i in range(len(cli)):
        while(cli[i]>0):
            li[j]=i
            cli[i]-=1
            print(cli)
            j+=1
    print("Actual list: ",li)

countsort([6,5,4,4,7,3,3,1,2,2,9])
