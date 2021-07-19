#Let's write a function to find missing numbers in range 1 to 100

import array as arr

def miss_num(a):  #funtion to find the missing numbers
    missing_num=arr.array('i',[])
    for i in range(a[0],a[-1]+1):
        if i not in a:
            missing_num.append(i)
    return missing_num


a=arr.array('i',[1,2,5,6,10])
print("The original array :",a)
print("The missing numbers in the array are :",miss_num(a))
