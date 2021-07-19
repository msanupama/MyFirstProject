#Let's write a program to add all the numbers in an array.



import array as arr 
def _sum(a):              #function to find the sum of numbers in array
    sum=0
    for i in a:
        sum=sum+i
    return sum





a=arr.array('i',[1,2,3,4,5,6,7])
print(a)
print("The sum of all the numbers in the array is :",_sum(a))
