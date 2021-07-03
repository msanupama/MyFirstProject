#print even and odd numbers
#Let's Consider printing even and odd numbers between 1 to 20

evenlist=[]
oddlist=[]
n=0
for n in range(1,21):
    if n%2==0:
        evenlist.append(n)
    else:
        oddlist.append(n)

print("The even numbers between 1 and 20 are  : \n",evenlist)
print("The odd numbers between 1 and 20 are  : \n",oddlist)

