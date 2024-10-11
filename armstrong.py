def main():
    
    num=int(input())
    temp=num
    c=len(str(num))
    arm=0
    while(temp!=0):
        r=temp%10
        arm=arm+(r**c)
        temp//=10
    if(num==arm):
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

if __name__ == "__main__":
    main()
