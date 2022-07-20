########## answer 1 #################
num=input("enter the num:")
if(num[::-1]==num):
    print("yes")
else:
    print("no")

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
             

########### answer 2 ########
factorial=1
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
   
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
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

      print("*",end =" ")
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


############# ANSWER 10 ############

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
print("total sum of all elements in list:",sum)

################ answer 12 ############
print()
print("########### ANSWER 12 (average,max) #############")
print()
num=int(input("num:"))
sum=0
l1=[]
for x in range(num):
  a=input("enter number")
  sum=int(sum) + int(a)
  
  l1.append(a)

print("sum:",sum)
average=sum/num
print("average :",sum,"/",num,":",average)
print("max of list:",max(l1))
print("min of list:",min(l1))

############## answer 14 ###################

def dictionary(l1,l2,l3):
    result=[{x:{y:z}} for (x,y,z) in zip(l1,l2,l3)]
    return result
s1=[]
num=int(input("num:"))
for x in range(num):
  a=input("enter number")
  s1.append(a)
print("s1:",s1)
s2=[]
num=int(input("num:"))
for y in range(num):
  a=input("enter number")
  s2.append(a)
print("s2:",s2)
s3=[]
num=int(input("num:"))
for z in range(num):
  a=input("enter number")
  s3.append(a)
print("s3:",s3)
print("original string:")
print("s1:",s1)
print("s2:",s2)
print("s3:",s3)
print("nested dictionary:")
ch='a'
print( "result",dictionary(s1,s2,s3))



############ answer 15 ##############


s1=set()
n=int(input("num:"))
for x in range (n):
    x=input("enter number or string:")
    s1.add(x)
print("s1:"s1)
s2=set()
m=int(input("num:"))
for y in range (m):
    y=input("enter the number or string of set:")
    s2.add(y)
print("s2:",s2)
print()
print("s2 is subset of s1",s1.issubset(s2))
print("s1 is subset of s2",s1.issubset(s2))
print("subset not exist")


######### answer 16 #####################

s1=set()
n=int(input("num:"))
for x in range (n):
    x=input("enter number or string:")
    s1.add(x)
print("s1:",s1)
s2=set()
m=int(input("num:"))
for y in range (m):
    y=input("enter the number or string of set:")
    s2.add(y)
print("s2:",s2)
r1=s1.difference(s2)
print("set differnce s1-s2 :",r1)
r2=s2.difference(s1)
print("set differnce s2-s1 :",r2)
t1=s1.symmetric_difference(s2)
print("symmetric differnce s1-s2 :",t1)
t2=s2.symmetric_difference(s1)
print("symmetric differnce s2-s1 :",t2)






############## ANSWER 17 #########

def Remove(tuples):
    for i in tuples:
        if(len(i)==0):
            tuples.remove(i)
    return tuples

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
        ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples)) 


########## ANSWER 18 ################3
print("17.")
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)

############### ANSSWER 19 ###############
lower, upper, special, digit = 0, 0, 0, 0
password = input("Enter your password")
if (len(password) >= 6):
    for i in password:
        for word in password.split():
            if(word[0].isupper()):
                upper += 1
        if(i.islower()):
            lower += 1
        if(i.isdigit()):
            digit += 1
        if(i == '@' or i == '$' or i == '_' or i == '#' or i=='&'):
            special += 1
else:
    print("Password should be more than 6 characters")
if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
    print("Valid Password")
else:
    print("Invalid Password")
















 
