p=21
flag=False
if p>1:
          
    for i in range(2,p):
        if (p%i)==0:
            flag=True
            break

    if flag:
        print(p, " is not a prime number")
    else:
        print(p, " is a prime number")
    

