#To illustrate Inheritance in Python.

class A:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def methodA(self):
        print("the value of class A variables :",self.a,self.b,self.c)
    def add(self,a=None,b=None,c=None):    #Method Overloading
        
        sum=0
        if a!=None and b!=None and c!=None:
            sum=self.a+self.b+self.c
        elif a!=None and b!=None:
            sum=self.a+self.b
        else:
            sum=self.a
        print("The sum is :" ,sum)
    def display(self):                           #Method Overriding
        print("This is a method from class A")
           
    

class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d
        
    def methodB(self):
        print("the value of class B variables :",self.a,self.b,self.c,self.d)
    def add(self,a=None,b=None,c=None,d=None):       #Method Overloading
        sum=0
        if a!=None and b!=None and c!=None and d!=None:
            sum=self.a+self.b+self.c+self.d
        elif a!=None and b!=None and c!=None:
            sum=self.a+self.b+self.c
        elif a!=None and b!=None:
            sum=self.a+self.b
        else:
            sum=self.a
        print("The sum is :" ,sum)
    def display(self):                             #Method Overriding
        print("This is a method from class B")


class C(B):
    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c,d)
        self.e=e
        
        
    def methodC(self):
        print("the value of class C variables :",self.a,self.b,self.c,self.d,self.e)
    def add(self,a=None,b=None,c=None,d=None,e=None):   #Method Overloading
        sum=0
        if a!=None and b!=None and c!=None and d!=None and e!=None:
            sum=self.a+self.b+self.c+self.d+self.e
        elif a!=None and b!=None and c!=None and d!=None:
            sum=self.a+self.b+self.c+self.d
        elif a!=None and b!=None and c!=None:
            sum=self.a+self.b+self.c
        elif a!=None and b!=None:
            sum=self.a+self.b
        else:
            sum=self.a
        print("The sum is :" ,sum)
    def display(self):                          #Method Overriding
        print("This is a method from class C")

a1=A(10,20,30)
b1=B(50,60,70,80)
c1=C(1,2,3,4,5)
a1.methodA()
b1.methodB()
c1.methodC()
print("The result of additon from B class:")
b1.add(40,50,60,70)
print("The result of additon from C class:")
c1.add(1,2,3,5)
b1.display()
c1.display()            #illustrates method overriding.
print("variable values of Parent class A.")
print(a1.a)
print(a1.b)
print(a1.c)
print("variable values of Child class B.")
print(b1.a)
print(b1.b)
print(b1.c)
print(b1.d)
print("variable values of Sub-class class C.")
print(c1.a)
print(c1.b)
print(c1.c)
print(c1.d)
print(c1.e)
