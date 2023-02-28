#class and function attributes

class Item:
    payrate=0.8                                 #class attribute

    def __init__(self,name,price,quantity):     # constructor
        
        #assertions
        assert price>=0
        assert quantity>=1

        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity
    
    # class function or method
    def calculate_total_price(self):
        return self.price*self.quantity
    

    # class method
    def apply_discount(self):
        self.price=self.price * self.payrate

    
    
item1=Item("Phone",100,7)
item1.apply_discount()
print(item1.price)

item2=Item("Laptop",200,3)
item2.payrate=0.5
item2.apply_discount()
print(item2.price)
