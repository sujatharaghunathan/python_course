# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 09:20:34 2019

@author: sujat
"""

from datetime import datetime
odds = [1,3,5,7,9,11,13,15,17]
right_this_minute = datetime.today().minute
if right_this_minute in odds:
    print("This minute seems a little odd")
else:
    print("Not an odd minute")