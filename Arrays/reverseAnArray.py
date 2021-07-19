#Let's write a program to reverse an array of values

import array as arr

def revers(a):       #function 1 to reverse an array
    return a[::-1]

def rev2(a):          #function 2 to reverse an array
    l=len(a)
    for i in range(int(l/2)):
        a[i],a[-i-1]=a[-i-1],a[i]
    return a
        
        


a=arr.array('i',[1,2,3,4,5,6,7])
print("The original array :",a)
print("The reversed array :",revers(a))

print("The reversed array 2 :",rev2(a))

