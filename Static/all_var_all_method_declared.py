class Calc:
    c=30                     #Class Variable Declaration
    d=40                     #Class Variable Declaration
    def __init__(self):      #Constructor Declaration
        self.a=20            #Instance Variable Declaration
        self.b=10            #Instance Variable Declaration
    def display(self):        #Instance Method Declaration
        print("The value of 2 Instance variables are : ",self.a, " and " ,self.b)
    def typedis(self):
        print("The data type of the 2 variables are : ", type(self.a), " & ",type(self.b))
    @classmethod
    def add(cls):
        print("Addition of 2 numbers is : ", cls.c+cls.d)
    @classmethod
    def sub(cls):
        print("Subtraction of 2 numbers is : ",cls.d-cls.c)
    @staticmethod
    def prod():
        print("The product of 2 numbers is : ",Test.c*Test.d)
    @staticmethod
    def div():
        print("The result of division is : ",Test.d/Test.c)


cc1=Calc()









