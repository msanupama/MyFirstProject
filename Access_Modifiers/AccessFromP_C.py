#To access variables and methods from 'parent_child' module.

from parent_child import *

class D:
    def __init__(self):
        self._p=200


a2=A()
print(a2._a)
a2._methodA()

a3=A1()
print(a3._d)
a3._child_methodA1()
