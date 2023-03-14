#understanding class, objects and constructors

class Item:
    def __init__(self,name,price,quantity):     # constructor
        
        #assertions to ensure conditional input ( user cannot enter negative values of price and quantity)
        assert price>=0
        assert quantity>=1

        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity

item1=Item("Phone",100,1)
item2=Item("Laptop",200,5)
item3=Item("Tablet",500,2)

