#Let's write a program to copy an array into another

import array as arr

def _copy(a):
    b=a
    return b


a=arr.array('i',[1,2,3,4,5,6,7,8])

print("The original array a :",a)
print("The duplicate array b :",_copy(a))
