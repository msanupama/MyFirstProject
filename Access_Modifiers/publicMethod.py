#Let's create some public fields and methods to use them in a different package.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name of the student is : ",self.name)
        print("Age of the student is : ",self.age)

s1=Student('Anupama',35)

        
