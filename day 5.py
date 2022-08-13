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
f1()

##class and object

class record():
    def name(self):
        n=str(input("enter the name:"))
        print("name:",n)
obj=record()
obj.name()

### class and object with argument
class record():
    def num(self,a,b):
        
        print(a+b)
obj=record()
obj.num(7,8)



###constructor
class record():
    def __init__(self):
        num=int(input("num"))
        print(num)
    def name(self):
        n=str(input("name:"))
        print("student name:",n)
    def roll_no(self):
        no=int(input("roll no:"))
        print("roll no:",no)
obj=record()
obj.name()
obj.roll_no()

#### distructor

class record():
    def __init__(self):
        num=int(input("num"))
        print(num)
    def name(self):
        n=str(input("name:"))
        print("student name:",n)
    def roll_no(self):
        no=int(input("roll no:"))
        print("roll no:",no)
    def __del__(self):
        print('h')
obj=record()
obj.name()
del obj
obj.roll_no() 

####

class calculation():
    a=10
    b=20
    def __init__(self,a,b):
        a=self.a
        self.b=b
        print(a)
        print(b)
        
    def sub(self,a,b):
        
        print("subtraction:",a-b)
    def multi(self,a,b):
        
        print("multiply:",a*b)
obj=calculation(6,8)
obj.sub(7,5)
obj.multi(1,2)
"""


####global

class calculation():
    a=10
    b=20
    def __init__(self,a,b):
        a=self.a
        self.b=b
        print(a)
        print(b)
        
        
    def sub(self):
        global a
        a=2
        global b
        b=2
        print("subtraction:",self.a-self.b)
    def multi(self):
        
        print("multiply:",self.a*self.b)
obj=calculation(6,8)
obj.sub()
obj.multi()

print (a,b)

