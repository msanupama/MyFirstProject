#Let's write a method to find the second largest number in an array

import array as arr

def sorted(a):
    size=len(a)
    c=a
    b=[]
    lowest=0
    for i in range(0,size):
        for j in range(i+1,size):
            if c[i]>c[j]:
                c[i],c[j]=c[j],c[i]
    return c,c[-2]

        




a=arr.array('i',[100,15,99,78,22,54,65,76,87])
print("The original array is : ",a)
print("The sorted array is : ",sorted(a)[0])
print("The second largest of the array is : ",sorted(a)[1])








