#Let's write a program to remove duplicates from an array

import numpy as np

a=np.array([1,1,2,2,3,3,4,4,5,5])
uniqa=set(a)
print("The original array : ",a)
print("The array with duplicates removed : ",uniqa)
