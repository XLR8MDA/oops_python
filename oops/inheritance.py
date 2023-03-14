#parent class
class Animal:
    def walk(self):
        print('Animal has 4 legs')

#child class
class Dog(Animal):
    def Bark(self):
        print('bark from dog')

dog=Dog()  #object declaration
dog.Bark() #child method
dog.walk() #parent method via inheriting parent properties
