#Let's call the public fields and methods from 'publicMethod'.

from publicMethod import *

class College:
    def __init__(self,rollno):
        self.rollno=rollno
    def roll_display(self):
        print("The Roll no of the student is :",self.rollno)

c1=College(21)

c1.roll_display()

s1=Student('Priyanka',39)
s1.display()
