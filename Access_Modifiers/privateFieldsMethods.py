#To illustrate private methods and private variables
class Hello:
    
    
    def __init__(self):
        self.a=10
        self.b=20
        self.__c=30       #private variable declaration

    def public_method(self):
       print(self.a)
       print(self.b)
       print(self.__c)
       self.__private_method()   #A private method call inside the class.

    def __private_method(self):  #Private method Declaration.
        print("private")
        print(self.a)
        print(self.__c)

h=Hello()
print(h.a)
print(h.b)
#print(h.__c)         #Accessing private variable outside the class results in an error.
h.public_method()
#h.__private_method()  #Accessing private method outside the class results in an error.
