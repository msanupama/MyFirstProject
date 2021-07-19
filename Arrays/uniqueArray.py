#Let's write a program to remove duplicates and print only unique elements
#of the array

import numpy as np

a=np.array([1,1,2,2,3,3,4,4,5,5,6,7,8,9,10])

uniqa=np.array(list(set(a)))
print("The original array is : ",a)
print("The new array with uniques elements is :",uniqa)

