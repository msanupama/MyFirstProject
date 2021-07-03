s="madam"

def reverse(s):
    str1=""
    for i in s:
        str1=i+str1
    print(str1)
    return str1
print("The original string is : ",s)
print("The reversed string is : ",reverse(s))

if s==reverse(s):
    print("The given string is a palindrome.")

else:
    print("The given string is not a palindrome.")

