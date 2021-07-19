#Let's create an array and find the index of a number

import array as arr

a=arr.array('i',[1,2,3,4,5,6,2,7,7])
print(a)
print(a.index(2))  #prints the index of the first occurence of 2 in the array
print(a.index(7))  #prints the index of the first occurence of 7 in the array

