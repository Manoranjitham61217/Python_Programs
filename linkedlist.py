class Node:
    def __init__(self,val):
        self.Value=val
        self.Next=None
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def Insert_end(self,Value):
        NewNode=Node(Value)
        if self.head==None:
            self.head=NewNode
            self.tail=self.head
            #self.tail.Next=self.head #forcircular
        else:
            #NewNode.Next=self.tail.Next #forcircularsingularly
            self.tail.Next=NewNode
            self.tail=NewNode
        self.Display()
      
    def Insert_begin(self,Value):
        NewNode=Node(Value)
        if self.head==None:
            self.head=NewNode
            self.tail=self.head
            #Self.tail.Next=self.head #forcircular
        else:
            NewNode.Next=self.head
            self.head=NewNode
        self.Display()

    def Insert_position(self,pos,Value):
        NewNode=Node(Value)
        if self.head==None:
            self.head=NewNode
            self.tail=self.head
            #Self.tail.Next=self.head #forcircular
        else:
            temp=self.head
            cpos=0
            while(cpos<pos-1):
                temp=temp.Next
                cpos+=1
            NewNode.Next=temp.Next
            temp.Next=NewNode
        self.Display()

    def Delete_begin(self):
        if self.head==None:
            print("Linked List dosen't exist")
        else:
            self.head=self.head.Next
        self.Display()

    def Delete_end(self):
        if self.head==None:
            print("Linked List dosen't exist")
        else:
            temp=self.head
            while(temp.Next!=self.tail):
                temp=temp.Next
            temp.Next=self.tail.Next
            self.tail=temp
        self.Display()

    def Delete_position(self,position):
        if self.head==None:
            print("Linked List dosen't exist")
        else:
            temp=self.head
            c=0
            while(c<position-1):
                temp=temp.Next
                c+=1
            temp.Next=temp.Next.Next
        self.Display()

    def linear_search(self, key):
        temp = self.head
        index = 0
        while temp:
            if temp.Value == key:
                return index
            temp = temp.Next
            index += 1
        return -1

    def selection_sort(self):
        if self.head==None:
            print("Linked List dosen't exist")
        else:
            temp=self.head
            while temp:
                min_node=temp
                min_prev=None
                ptr=temp.Next
                while ptr:
                    if ptr.Value<min_node.Value:
                        min_node=ptr
                        min_prev=ptr
                    ptr=ptr.Next
                if min_node!=temp:
                    temp.Value,min_node.Value=min_node.Value,temp.Value
                temp=temp.Next
        print("Sorted linked list")
        self.Display()

    def reverse(self):
        prev=None
        temp=self.head
        while(temp is not None):
            self.Next=temp.Next
            temp.Next=prev
            prev=temp
            temp=self.Next
        self.head=prev
        print("Reveresed Linked list")
        self.Display()
        
    def Display(self):
        temp=self.head
        while(temp!=None):
            print(temp.Value,end="->")
            temp=temp.Next
        print(temp)

object=linked_list()
object.Insert_end(5)
object.Insert_end(8)
object.Insert_end(3)
object.Insert_end(6)
object.Insert_end(2)

object.selection_sort()
key=6
result=object.linear_search(key)
if result!= -1:
    print("Element ",key, " found at index:", result)
else:
    print("Element not found")
object.reverse()
