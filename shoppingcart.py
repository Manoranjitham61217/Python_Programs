class cart:
    p_dict={"MILK":37,"RICE":70,"APPLE":100,"SUGAR":50,"OIL":110}
    def __init__(self,Name):
        print(self.p_dict)
        self.Name=Name
        self.listcart=[]
    def add(self,proname):
        self.listcart.append(proname)
        print(self.listcart)
    def remove1(self):
        print(self.listcart)
        n=input("Removing Input:")
        self.listcart.remove(n)
        print(self.listcart)
    def billing(self):
        c=0
        for i in self.listcart:
            print(i,self.p_dict[i])
            c=c+self.p_dict[i]
        print("Total bill= ",c)
        
guna=cart("gunaseelan")
while(True):
    n=int(input("Enter Case:"))
    match n:
        case 1:
            guna.add(input("Adding Input:"))
        case 2:
            guna.remove1()
        case 3:
            guna.billing()
            break;
