#Let's write a program to find the difference between
#the smallest and largest value in an array

import array as arr

def diff(a):
    size=len(a)
    for i in range(size):
        for j in range(i+1,size):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    smallest,largest=a[0],a[-1]
    return a,largest-smallest
    



a=arr.array('i',[15,20,25,30,35,40,45,50,55,60,100,95,90,85,80,70])
print("The original array is :",a)
print("The sorted array is :",diff(a)[0])
print("The difference of the largest and the smallest values of the array is :",diff(a)[1])
