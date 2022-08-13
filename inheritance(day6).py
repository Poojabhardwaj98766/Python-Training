######### INHERITANCE #########
print("day 6")

print("single Inheritance")
class A:
    a=10
    b=30
    def add(self):
        a=int(input("a:"))
        b=int(input("b:"))
        print(a+b)
class B(A):
    def sub(self):
        a=self.a
        b=self.b
        print(a-b)

ob=B()
ob.add()
ob.sub()

####### MUTILEVEL INHERITANCE #########
print()
print("multilevel Inheritance")
print()
class A:
    a=10
    b=30
    def add(self):
        a=int(input("a:"))
        b=int(input("b:"))
        print("a+b=",a+b)
class B(A):
    def sub(self):
        a=self.a
        b=self.b
        print("a-b=",a-b)
class C(B):
    def mul(self):
        global a
        a=int(input("a:"))
        global b
        b=int(input("b:"))
     
        print("a*b=",a*b)
ob=C()
ob.add()
ob.sub()
ob.mul()

############# MULTIPLE INHERITANCE ############
print()
print("multiple Inheritance")
print()
class A:
    a=10
    b=30
    def add(self):
        a=int(input("a:"))
        b=int(input("b:"))
        print("a+b=",a+b)
class B:
    def sub(self):
        a=self.a
        b=self.b
        print("a-b=",a-b)
class C(A,B):
    def mul(self):
        global a
        a=int(input("a:"))
        global b
        b=int(input("b:"))
     
        print("a*b=",a*b)
ob=C()
ob.add()
ob.sub()
ob.mul()


########## HIERARECIAL INHERITANCE #################
print()
print("multiple Inheritance")
print()
class A:
    a=10
    b=30
    def add(self):
        a=int(input("a:"))
        b=int(input("b:"))
        print("a+b=",a+b)
class B(A):
    def sub(self):
        a=self.a
        b=self.b
        print("a-b=",a-b)
class C(A):
    def mul(self):
        global a
        a=int(input("a:"))
        global b
        b=int(input("b:"))
     
        print("a*b=",a*b)
ob1=B()
ob2=C()
ob1.add()
ob1.sub()
ob2.mul()
ob2.add()


########## HYBRID INHERITANCE #################
print()
print("***Hybrid Inheritance***")
print()
class A:
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    d=int(input("d:"))
   
    def add(self):
        a=self.a
        b=self.b 
        print("a+b=",a+b)
class B(A):
    def sub(self):
        a=self.a
        b=self.b
        print("a-b=",a-b)
class C(B):
    def mul(self):
        global a
        a=int(input("a:"))
        global b
        b=int(input("b:"))
     
        print("a*b=",a*b)
class D(C):
    def div(self):
        a=self.a
        b=self.b
        print("a/b",a/b)
class E(C):
    def modulas(self):
        global c
        c=int(input("c:"))
        global d
        d=int(input("d:"))
        print("c%d:",c%d)
     
        print("c*d=",c*d)
class F(D,E):
    def compare(self):
        a=self.a
        b=self.b
        if(a>b):
            print(a,"is greater than",b)
        else:
            print(a,"is lesser than",b)
       
class G(F):
    def result(self):
        print("calculation competed")
ob1=C()
ob2=F()
ob=G()
ob1.add()
ob1.sub()
ob1.mul()

ob2.add()

ob2.compare()


ob2.add()
ob.result()
print(issubclass(D,E))
print(isinstance(D,E))

#########   SUPER keyword and SELF KEYWORD ##############
print()
print("super keyword")
print()
class A:
    a=int(input("a:"))
    b=int(input("b:"))
    
    def add(self):
        a=self.a
        b=self.b 
        print("a+b=",a+b)
class B(A):
    def sub(self):
        super().add()
        
        
        print("a-b=",super().a-super().b)
        
ob=B()
ob.add()
ob.sub()
