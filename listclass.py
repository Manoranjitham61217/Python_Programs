class CustomList:
    def __init__(self) -> None:
        self.li = []

    def appending(self, a):
        self.li.append(a)

    def inserted(self, index, a):
        self.li.insert(index, a)

    def poping(self, index):
        return self.li.pop(index)

    def removing(self, a):
        self.li.remove(a)

    def length(self):
        return len(self.li)

    def display(self):
        print(self.li)
        
at = CustomList()
at.appending(1)
at.appending(2)
at.appending(3)
at.appending(4)
at.appending(5)
at.display()

at.inserted(3, 6)
at.inserted(4, 7)
at.display()

at.poping(3)
at.display()

at.removing(2)
at.display()

at.removing(7)
at.display()

print(f"Length of list: {at.length()}")                                                                       
