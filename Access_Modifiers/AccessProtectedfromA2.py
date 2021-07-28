#To illustrate how Protected variables and methods are used in Python

class A:                   #A Class

    def __init__(self):
        self._a=10
        self._b=20              #Protected Variables in A

    def _methodA(self):       #Protected Method in A
        print("This is a protected method from class A")


a1=A()
print(a1._a)

class B:                  #B Class
    def __init__(self):
        self._c=30           #Protected variable in Class B

    def _methodB(self):      #Protected method in Class B
        print("This is a protected method from class B")

b=B()
print(b._c)              #Printing the variable of the same class
b._methodB()              #Calling method of the same class
print('*'*60)
a2=A()                       #Instance of A Class in B Class.
a2._methodA()            #Calling protected method of Class A from Class B.
print(a2._a)       #Printing the value of Protected variable from Class A.
print(a2._b)              
        
    
