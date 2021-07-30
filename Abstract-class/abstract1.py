#Create abstract classes, abstract methods amd non-abstract methods.

from abc import ABC, abstractmethod

class Person:                   #abstract class

    @abstractmethod
    def work(self):                 #abstract method
        print("This is an abstract method.")

    def __init__(self,name,age,edu):
        self.name=name
        self.age=age
        self.edu=edu

    def bio(self):
        print("Name of the person is: ",self.name)
        print("Age of the person is: ",self.age)
        print("Education of the person is: ",self.edu)
