# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 08:30:25 2019

@author: sujat
"""

word = 'Hello World'
vowels = ['a','e','i','o','u']
found = []
for i in word:

    if i in vowels:
        if not i in found:
            found.append(i)
            print(i)
 
print(found)   
    
    