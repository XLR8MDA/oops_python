class Animal:                                   # Parent class
        
    def make_sound(self):                       # parent method
        print("Some generic animal sound makes parent class")

class Dog(Animal):                              # Child class
        
    def make_sound(self):                        # child method

        print("Woof!")

dog=Dog()                                       # create an object of child class

dog.make_sound()                                # calls only child method

Animal.make_sound(dog)                          # calls only parent method without using super



''' using super will call both parent and child method

    super().make_sound() # calls both parent and child method

    change the make_sound() function in child class Dog by adding super().make_sound() line     '''