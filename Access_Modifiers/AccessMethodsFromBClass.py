#To access methods from other classes in the same package.

class A:
    def __init__(self):
        self.a=12
        self.b=13
        self.c=14

    def methoda(self):
        print("Method from Class A")
        self.d=15
        print(self.d)
        print(self.a)
a=A()
print(a.a)
print(a.b)
a.methoda()



class B:
    def __init__(self):
        self.a=18
        self.b=19
        self.c=20

    def methodb(self):
        print("Method from Class B")
        self.d=21
        print(self.d)
        a2=A()          #Object of class A in B
        a2.methoda()       #Calling method of A in B


b=B()
print(b.a)
print(b.b)
b.methodb()
