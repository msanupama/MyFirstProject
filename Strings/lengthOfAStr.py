#Let's write a program to find the length of a string.

#We will illustrate 2 ways of finding the length of a string in Python

#The first method: Let's use for loop.

my_str="Hello"
counter=0

for i in my_str:
    counter+=1
print(counter)


#The second method: We use a built-in method called len()

my_str="Hello"

counter=len(my_str)
print(counter)
