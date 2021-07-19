#Let's write a function to find duplicate elements in an array

import array as arr

def repeat(x):
    size=len(x)
    repeated=[]

    for i in range(size):
        k=i+1
        for j in range(k,size):
            if x[j]==x[i]:
                repeated.append(x[i])

    return repeated



x=arr.array('i',[10,20,30,40,10,40,20,30,4,5])
print("The original array :",x)
print("The duplicate elements in the array: ",repeat(x))
