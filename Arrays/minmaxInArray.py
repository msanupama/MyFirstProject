#Let's write a function ot find min and max values in an array

import array as arr

def minmax():
    maxm=a[0]
    minm=a[-1]

    for i in a:
        if i>maxm:
            maxm=i
        elif i<minm:
            minm=i
    return (maxm,minm)

a=arr.array('i',[1,2,3,4,5,6,7])

print("The max and min values of the array are : ", minmax())
