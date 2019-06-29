# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 08:04:21 2019

@author: sujat
"""

import random
random_num = []
for (x) in range(10):
    number = random.randint(1,10)
    random_num.append(number)
    print(number)
    
sum_rand = 0
for i in range(10):
    sum_rand = sum_rand+random_num[i]
    
average = sum_rand/10
print(average)
     
    