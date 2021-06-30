class Calc:
    c=12      #Class Var Declaration
    d=13       #Class Var Declaration
    def __init__(self):
        self.a=10           #Instance Var Declaration
        self.b=11            #Instance Var Declaration
c1=Calc()
print(c1.a)          #prints Instance var in main
print(c1.b)          #prints Instance var in main
print(Calc.c)         #prints Class/Static var in main
print(Calc.d)         #prints Class/Static var in main
