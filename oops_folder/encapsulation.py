#understanding encapsulation with access modifiers

class Car:
    def __init__(self,Name,Model,Year):
        self.name=Name          #public 
        self.__model=Model      #private 
        self._year=Year         #protected

    def get_model(self):
            return self.__model
    def set_model(self,Model):
            self.__model=Model

       
    
car=Car("Hundai",'old',2000)
print(car.name)                 #calling public  
print(car._year)                #calling protected
print(Car.get_model(car))       #calling private using getter
Car.set_model(car,"new")        #value of model changed using setter 
print(car.get_model())          #printing new value of model