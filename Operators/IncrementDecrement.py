#Let's write a methods for increment and decrement operators
#In python increment and decrement operators are not seen as i++ and i--
#They can be seen as += and -=

def inc():
    i=0
    while (i<=10):
        print(i)
        i+=1        #increment operator in Python

def dec():
    i=10
    while (i>=0):
        print(i)
        i-=1        #decrement operator in Python






print("The numbers 1 to 10 : ",inc())
print("The numbers 10 to 1 : ",dec())
