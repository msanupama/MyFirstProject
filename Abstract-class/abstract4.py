#Create an instance of the child class in child class and call non-abstract methods.

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
        print("Name of the teacher is: ",self.name)
        print("Age of the teacher is: ",self.age)
        print("Education of the teacher is: ",self.edu)
                 
        
    def work(self,p2):         #Abstract method in child class
        print("The work of of a teacher is to teach")
        p2.bio()                #Calling non-abstract method in the class.

    

t1=Teacher('Master',26,'B.Ed')
t1.work(t1)
