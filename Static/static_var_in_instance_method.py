class Calc:
    c=40    #Static/Class variables Declaration
        
    def __init__(self):
        Calc.d=50
    def display(self):     #Instance MEthod
        print("The values of the Class/Static variables are : ",Calc.c," & ",Calc.d)
    
        


c1=Calc()
c1.display() #Prints Static variables in Instance method
      
    
