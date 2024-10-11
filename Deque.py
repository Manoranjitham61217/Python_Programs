class deque:
    def __init__(self,size):
        self.size=size
        self.deqli=[]

    def isFull(self):
        if(len(self.deqli)==self.size):
            return True
        return False

    def Append(self,val):
        if isFull():
            print("Queue is Full")
        else:
            self.deqli+=[None]
            self.deqli[-1]=val

    def AppendLeft(self,val):
        if isFull():
            print("Queue is Full")
        else:
            self.deqli=[None]+self.deqli
            self.deqli[-1]=val

    def isEmpty(self):
        if self.deqli==[]:
            return True
        return False

    def Pop(self):
        if isEmpty():
            print("Queue is empty")
        else:
            x=self.deqli[-1]
            self.deqli[-1]=[None]
            del(self.deqli[-1])
        return x

    def PopLeft(self):
        if isEmpty():
            print("Queue is empty")
        else:
            x=self.deqli[0]
            self.deqli[0]=[None]
            del(self.deqli[0])
        return x

Que=deque(5)
print('1-append,2-appendLeft,3-pop,4-popLeft,5-Full,6-Empty,7-exit')
while(1):
    cas=int(input())
    match cas:
        case 1:
            
