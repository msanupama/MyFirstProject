#Create an instance of the child class in child class and call abstract methods.

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

    def bio(self,p1):
        print("Name of the person is: ",self.name)
        print("Age of the person is: ",self.age)
        print("Education of the person is: ",self.edu)
        p1.work()          #Calling Abstract method in Class
        
    def work(self):         #Abstract method in child class
        print("The work of of a teacher is to teach")

t1=Teacher('Master',26,'B.Ed')
t1.bio(t1)
