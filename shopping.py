class shopping_cart:

        def __init__(self,items):
            self.items=items
            items=list()

        def add(self):
            self.items.append()

        def remove(self):
            self.items.remove()

        def display(self):
            return shopping_cart.items()

        def Available_items(self, grocery, vegetables, fruits,snacks,stationary):
            self.grocery=({Dal,76},{Sugar,54},{Oil,110},{masalas,50})
            self.vegetables=({Tomato,40},{Onion,55},{Potato,80},{Carret,60})
            self.fruits=({Apple,120},{Grapes,75},{Orange,90},{Banana,50})
            self.snacks=({Biscuit,20},{Chips,10},{sweets,100},{Bread,30})
            self.stationary=({Note,50},{Pen,20},{Box,60})


item1=shopping_cart("Apple")
item2=shopping_cart("Tomato")
item3=shopping_cart("Dal")
item4=shopping_cart("Sugar")
item5=shopping_cart("Chips")

print(item1.display())
print(item2.display())
print(item3.display())
print(item4.display())
print(item5.display())
