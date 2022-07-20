"""a=23
def f():
    print('f1',a)
def g():
    a=20
    print('g',a)
def h():
    global a
    a=30
    print('h',a)
print('glo',a)
f()
print('glo',a)
g()
print('glo',a)
h()
print('glo',a)

def f1():
    a=10
def f2():
    print('hello')
    nonlocal a
    a=40
    print()
    f2()
f1()"""

##class and object

class record():
    def name(self):
        n=str(input("enter the name:"))
        print("name:",n)
obj=record()
obj.name()

###
class record():
    def num(self,a,b):
        
        print(a+b)
obj=record()
obj.num(7,8)
