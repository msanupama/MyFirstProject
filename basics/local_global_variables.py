a=12
print("Value of a is :",a)

def func():
    
    global a
    a=20
    print("Value of a is :",a)

func()
print("Value of a is :",a)
