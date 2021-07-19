#Let's write a function to insert a value at a specific index in an array

import array as arr

def ins(a):         #Function to insert a value in the array
    a.insert(2,10)
    return a
     
    


a=arr.array('i',[1,2,3,4,5,6,7])
print("The original array : ",a)
print("The altered array : ",ins(a))
