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
print('glo',a)"""

def f1():
    a=10
def f2():
    print('hello')
    nonlocal a
    a=40
    print()
    f2()
f1()
          