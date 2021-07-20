#Let's write a program to illustrate equals and not equals operators

#Let's print even and odd numbers using equals and not-equals operators.

def even():
    i=1
    print("Even numbers between 1 and 10 : ")
    while i<=10:
        if i%2 == 0:      #equals operator
            print(i)
        i+=1
        
   

def odd():
    i=1
    print("Odd numbers between 1 and 10 : ")
    while (i<=10):
        if i%2!=0:        #not-equals operator
            print(i)
        i+=1


#Let's call the function to print even numbers
even()

#Let's call the function to print odd numbers
odd()  
