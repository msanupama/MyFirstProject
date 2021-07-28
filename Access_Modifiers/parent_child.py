#To access Protected methods and variables from child class in another package.

class A:
    def __init__(self):
        self._a=20
        self._b=30
        self._c=40
    def _methodA(self):
        print("This is a method from class A")
        print("The value of the variable a is :",self._a)


class A1(A):

    def __init__(self):
        self._d=50
        self._e=60
    def _child_methodA1(self):
        print("This is the child-class method A1 of A")
        print(self._d,self._e)

