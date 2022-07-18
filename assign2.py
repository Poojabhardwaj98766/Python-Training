"""########## answer 1 #################
num=input("enter the num:")
if(num[::-1]==num):
    print("yes")
else:
    print("no")"""

############# answer 5 ############

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
     choice=input("enter the operation(1,2,3,4):")
     if choice in ('1','2','3','4'):
           a=float(input("a="))
           b=float(input("b="))
           if choice=='1':
               print("add", add(a,b))
               
           elif(choice=='2'):
                print ("sub:",sub(a,b))
                       
           elif(choice=='3'):
                print ("mul",mul(a,b))
                
           elif(choice=='4'):
                print( "div=",div(a,b))
                
           else:
                print("default")
     else:
             print("invalid")
`11`
              

########### answer 2 ############

"""factorial=1
num=int(input("enter the value of num:"))
if num<0:
          print("invalid number")
elif num=='0':
    print("factorial of 0 : 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of",num,":",factorial) 

############ answer 3###############
print()
print("########### answer 3 #############")
print()
n=int(input("n="))
def Fibonacci(n):
    if n < 0:
        print("invalid input")
    elif n == '0':
        return 0
    elif n =='1' or n =='2':
        return 1
    else:
          return Fibonacci(n-1) + Fibonacci(n-2)
        
print(Fibonacci(n))
 ###################################################

n=int(input("n="))
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(n))

##############matrix pattern###############
print()
print("######### matrix pattern ################")
print()
for x in range(5):
    for y in range(6):

      print("*",end=" ")
    print()


############ traingle pattern ##############
print()
print("############ traingle pattern ##############")
print()
n=int(input("n="))
for x in range(n):
   for y in range(0,x+1):

      print("*",end=" ")
   print()
########### REVERSE PATTERN #############
print()
print("########### REVERSE PATTERN #############")
print()
n=int(input("n="))
for x in range(n):
   for y in range(x,n):

      print("*",end=" ")
   print()

############ pyramid pattern##############       

print()
print("########### PYRAMID PATTERN #############")
print()
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

############### answer 7 ##################

print()
print("########### Answer 7 (leap year) #############")
print()
year=int(input("enter the year:"))
if year%4==0:
    print("given year",year,"is leap year")
else:
    print("not a leap year")


############## Answer 8 ##################

print()
print("########### ANSWER 8 (Prime num) #############")
print()
num=int(input("enter the number:"))
for i in range (1,num-1):
    if(num%i==0):
     print(i)
    else:
         print(num,"is a prime number")
 

############## ANSWER 9 ##############

print()
print("########### ANSWER 9 (FIND AREA) #############")
print()
l=float(input("enter the length :"))
b=float(input("enter the breadth:"))
area=l*b
print("area:",area)


############# ANSWER############

print()
print("########### ANSWER 10 (REVERSE A LIST) #############")
print()
l1=[]
for x in range(5):
  a=input("enter number")
  l1.append(a)
print(l1)
new_list=l1[::-1]
print(new_list)


########### ANSWER 11  ################
num=int(input("num:"))
sum=0
l1=[]
for x in range(num):
  a=input("enter number")
  sum=int(sum) + int(a)
  print("sum:",sum)
  l1.append(a)
print(l1)
print("total sum of all elements in list:",sum)"""


















 
