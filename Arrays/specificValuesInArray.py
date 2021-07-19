#Let's write a method to verify if the array has the values [12,23] in it

import array as arr

def ispresent(x,y):
    if (x in a) and (y in a):
        print("The values ",x," and ",y," exist in the array.")
    elif (x in a) and (y not in a):
        print("Only the value ",x," exists in the array")
    elif (y in a) and (x not in a):
        print("Only the value ",y," exists in the array")
    else:
        print("Sorry, both the values ",x," and ",y," do not exist in the array.")

a=arr.array('i',[24,23,22,21,20,11,12,32,13,14])
ispresent(12,234)
        
