#Let's write a method to find the number of even and odd numbers in an array

import array as arr

def num_even(a): #function to find and count the even numbers
    size=len(a)
    even_no=0
    print("Even numbers in the array :")
    for i in range(size):
        if i%2==0:
            print(i)
            even_no+=1
    return even_no




def num_odd(a):   #function to find and count the odd numbers
    size=len(a)
    odd_no=0
    print("Odd numbers in the array :")
    for i in range(size):
        if i%2!=0:
            print(i)
            odd_no+=1
    return odd_no



a=arr.array('i',[1,2,3,4,5,6,7,8,9])
print("The original array : ",a)
print()
print()
print("The number of even numbers in the array are: ",num_even(a))
print("The number of odd numbers in the array are: ",num_odd(a))

