#Let's access Protected vars and methods from Class A in another package.

from parent_child import *

class C:
    def __init__(self):
        self._x=100

a1=A1()
print(a1._d)

