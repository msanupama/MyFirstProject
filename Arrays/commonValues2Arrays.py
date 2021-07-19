#Let's write a program to find common values btw 2 arrays

import array as arr

def common(x,y):
   
    xset=set(x)
    comvals=xset.intersection(y)
    return list(comvals)
    




x=arr.array('i',[1,2,3,4,5,6])
y=arr.array('i',[5,6,7,8,9,10])
print("The common values in the 2 arrays are : ",common(x,y))
