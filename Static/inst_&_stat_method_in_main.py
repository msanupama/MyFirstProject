class Calc:
    c=30
    d=40     #Class Vars DEclaration
    def __init__(self):
        self.a=10      #Instance vars Declaration
        self.b=20
    def display(self):   #Instance method
        print("The values of Instance variables a and b are : ",self.a," & ",self.b)
    @staticmethod
    def add():     #Static method
        print("Addition of Class variables is : ",Calc.c+Calc.d)
c1=Calc()
c1.display()      #Calling the instance method from main.
Calc.add()        #Calling Static method from main.


    
