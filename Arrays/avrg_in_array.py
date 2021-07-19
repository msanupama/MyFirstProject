#Let's write a program to calculate the average of all float numbers in an array

import array as arr

def avrg(a):        #function to find the average.
    sum=0
    l=len(a)

    for i in a:
        sum+=i
    return sum/l

a=arr.array('f',[1.1,2.2,3.3,4.4,])
print(a)
print("The average of all the numbers in the list :",avrg(a))
