print("############# TYPES OF ERRORS ######################")
print()
print("#### Syntax Error ####")
num=int(input("enter the num:"))
if(num>1000)
 print(num,"greater than 1000")


#======== OUTPUT =========
#syntax error : 

print("### Logical Error ###")
num=int(input("enter the num:"))
print(num/0)

#======== OUTPUT =========
#print(num/0)ZeroDivisionError: division by zero 

import mymodule
print("### Nmae Error ###")
print("my age is ",age)

# #======== OUTPUT =========
# # ModuleNotFoundError: No module named 'mymodule'

print("### type error ###")
geek = "Geeks"
num = 4
# it will generate type error becoz num can't be added to a string
print(geek + num + geek)


# #======== OUTPUT =========
# print(geek + num + geek)
# TypeError: can only concatenate str(not "int") to str

print("### index error ####")
l1 = [2, 4, 5, 6]
print(l1[5])  # index not present

# #======== OUTPUT =========

print("### key error ###")
dict = {
    1: "red",
    2: "blue",
    3: "green",
}
print(dict[4])  # 4 key doen't exist

# #======== OUTPUT =========
# TypeError: can only concatenate str(not "int") to str
# ^ ^ ^^
# SyntaxError: invalid syntax


print("### value error ###")
print(int("xyz"))  # invalid literal for int

#======== OUTPUT =========
# print(int("xyz"))  # invalid literal for int
# ValueError: invalid literal for int() with base 10: 'xyz'


print("### indentation error ###")
if (3 > 5):
print("hello")  # no space included before print

# #======== OUTPUT =========
# print("hello")  # no space included before print
# ^
# IndentationError: expected an indented block after 'if' statement


print("### modulenot found error ####")
list = [3, 5, 7, 9, 11]
print(list[3])

# #======== OUTPUT =========
# 9

print("###  attribut error  ###")
x = 10
print(x.append(6))  # int has no attribute append

# #======== OUTPUT =========
# print(x.append(6))  # int has no attribute append
# AttributeError: 'int' object has no attribute 'append'

