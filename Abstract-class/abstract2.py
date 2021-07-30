#Create a sub class for the abstract class,create an object in the child class
#for the abstract class and access the non-abstract methods.

from abc import ABC, abstractmethod

class Person(ABC):                   #abstract class

    @abstractmethod
    def work(self):             #abstract method
      
        pass

        
class Teacher(Person):
    def __init__(self,name,age,edu):
        self.name=name
        self.age=age
        self.edu=edu

    def bio(self):
        print("Name of the person is: ",self.name)
        print("Age of the person is: ",self.age)
        print("Education of the person is: ",self.edu)
        
    def work(self):         #Abstract method in child class
        print("The work of of a teacher is to teach")


t1=Teacher('April',23,'B.Ed')   #Constructor of the child class of the Abstract class
t1.bio()        #Non-Abstract method called from child class.
t1.work()       #Abstract method called from child class of the Abstract class



