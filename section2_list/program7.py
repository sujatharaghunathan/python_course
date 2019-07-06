# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 08:06:52 2019

@author: sujat
"""
import random
numbers = random.sample(range(0,100),10)
largest = 0
for (x) in numbers:
    if x > largest : 
        largest = x
        
print (largest)
        

import random
numbers = random.sample(range(0,100),10)
numbers.sort()
second_largest = numbers[8]
print(second_largest)

odd=[]
even=[]
import random
numbers = random.sample(range(0,500),100)

for (x) in numbers:
    if (x % 2) == 0:
        print(x)
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)

