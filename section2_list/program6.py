# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 08:45:03 2019

@author: sujat
"""

number =[10,2,3,4,'sujatha']
number.pop()
print (number)

number.pop(0)
print(number)

number.extend(["manish","antara","avantika"])
print(number)

number.insert(3,"sujatha")
print(number)

my_string = "Don't panic!"
mystring_list = list(my_string)
for i in range(4):
    mystring_list.pop()
mystring_list.pop(0)
mystring_list.remove("'")
mystring_list_temp = [mystring_list.pop(),mystring_list.pop()]
mystring_list.extend(mystring_list_temp)
temp_char = mystring_list.pop(3)
mystring_list.insert(2,temp_char)
print("".join(mystring_list))

letters = list("Don't Panic")
print(letters[0:10:3])
