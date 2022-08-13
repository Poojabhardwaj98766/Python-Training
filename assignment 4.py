#####Example 1
from abc import ABC, abstractmethod
class Animal(ABC):
        @abstractmethod
        def eat1(self):
                pass
        @abstractmethod
        def eat2(self):
                pass
class Tiger(Animal):
        def eat1(self):
                print("Tiger implementation ...")
class lion(Tiger):
        def eat2(self):
                print("lion implementation ...")
t = lion()
t.eat1()
t.eat2()

####### output ##########
Tiger implementation ...
lion implementation ...


Example 2
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
 	def __init__(self, value):
 		self.value = value
 		super().__init__()
 
 	@abstractmethod
 	def do_something(self):
 		pass
 
class DoAdd(AbstractClassExample):
        def do_something(self):
                return self.value + 42
 
class DoMul(AbstractClassExample):
        def do_something(self):
                return self.value * 42
 
x = DoAdd(10)
y = DoMul(10)
print(x.do_something())
print(y.do_something())

########### output ###########
52
420


Example 3 

def status(age):
 	if age < 0:
 		raise ValueError("Only positive integers are allowed")
 	if age>22:
 		print("eligible for mrg")
 	else:
 		print("not eligible for mrg try after some time")
try:
 	num = int(input("Enter your age: "))
 	status(num)
except ValueError:
 	print("Only positive integers are allowed you ......")
finally:
 	print("finally block....")

###### output ############
Enter your age: 25
eligible for mrg
finally block....


Enter your age: -1
Only positive integers are allowed you ......
finally block....


Enter your age: 18
not eligible for mrg try after some time
finally block....


Example 4

class NegativeAgeException(RuntimeError):
 	def __init__(self, age):
 		super().__init__()
 		self.age = age
def status(age):
 		if age < 0:
 			raise NegativeAgeException("Only positive integers are allowed")
 		if age>22:
 			print("Eligible for mrg")
 		else:
 			print("not Eligible for mrg....")
try:
 	num = int(input("Enter your age: "))
 	status(num)
except NegativeAgeException:
 	print("Only positive integers are allowed")
except:
 	print("something is wrong")

### output ############
Enter your age: 23
Eligible for mrg


##Example 5:

class TooYoungException(Exception):
        def __init__(self,age):
                self.age=age
class TooOldException(Exception):
        def __init__(self,age):
                self.age=age
try:
        age=int(input("Enter Age:"))
        if age<18:
                raise TooYoungException("Plz wait some time ")
        elif age>65:
                raise TooOldException("Your age too old")
        else:
                print("we will find one girl soon")
except TooYoungException as e:
 	print("Plz wait some time ")
except TooOldException as e:
 	print("Your age too old ")

###### output #######
Enter Age:67
Your age too old 


Example 6

try:
        print("outer try block")
        n = int(input("enter a number"))
        print(10/n)
        try:
                print("inner try")
                print("anu"+"preet")
        except TypeError:
                print("Hello")

        else:
                print("inner no exception")
except ArithmeticError:
        print(10/5)
else:
        print("outer no excepiton")
finally:
        print("finally block")

####### output ###########
outer try block
enter a number4
2.5
inner try
anupreet
inner no exception
outer no excepiton
finally block

        

Example 7

class Person(object):
 	def __init__(self, first, last):
 		self.firstname = first
 		self.lastname = last
 	def Name(self):
 		return self.firstname + " " + self.lastname
class Employee(Person):
	def __init__(self, first, last, staffnum):
		super().__init__(first,last)
		#Person.__init__(self,first, last)
		self.staffnumber = staffnum
	def GetEmployee(self):
		return self.Name() + ", " + self.staffnumber
x = Person("komal", "addanki")
y = Employee("komal", "addanki", "111")
print(x.Name())
print(y.GetEmployee())
####### output #######
komal addanki
komal addanki, 111


Example 8

class Person:
 	def __init__(self, first, last):
 		self.firstname = first
 		self.lastname = last
 	def __str__(self):
 		return self.firstname + " " + self.lastname
class Employee(Person):
 def __init__(self, first, last, id):
 		super().__init__(first, last)
 		self.id = id
 	def __str__(self):
 		return super().__str__()+" "+self.id
x = Person("kamalpreet", "gurpreet")
y = Employee("kamalpreet", "gurpreet", "111")
print(x)
print(y)

Example 9

class Vehicle:
 	def __del__(self):
 		print("Vehicle object destroyed")
 		print(10/1)
v = Vehicle()
del v

########## output #########
Vehicle object destroyed
10.0


Example 10

class Customer:
 	def __init__(self,name,bal=0.0):
 		self.name=name
 		self.bal=bal
 
 	def deposit(self,amount):
 		self.bal=self.bal+amount
 	def withdraw(self,amount):
 		if amount>self.bal:
 			raise RuntimeError("withdraw amount is more than balance")
 		else:
 			self.bal=self.bal-amount
 
 	def remaining(self):
 		return self.bal;
 
c = Customer("Komal",10000)
damt = int(input("enter amount to deposit"))
c.deposit(damt)
amt = int(input("enter amount to withdraw"))
c.withdraw(amt)
print(c.remaining())
#########3 output #############
enter amount to deposit
600
enter amount to withdraw100
10500
