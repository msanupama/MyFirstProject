#Let's write a program to match a string using match().
#match() function returns the match object if it occurs
#in the start of the string.

import re

my_str="Python and Java are good Programming Languages."

res=re.match(r'Python',my_str)  
print(res)

if res:
    print("Match found")
else:
    print("Match not found")
    
