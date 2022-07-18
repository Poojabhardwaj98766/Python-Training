num=int(input("enter the num"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
     print('YES')
else:
    print('no')


l1=[]
for x in range(5):
  a=input("enter number")
  l1.append(a)
print(l1)
"""s1=set(l1)
print(s1)
s1.add(12)
print(s1)

pop(4)
print(s1)"""

l2=input("enter the num that u want to insert:")


l1.insert(l2)
print(l1)
l3=input("enter the num that u want to remove:")
l1.remove(l3)
print(l1)
