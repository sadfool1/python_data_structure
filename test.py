#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:14:35 2020

@author: jameselijah
"""

mylist = input("Input your list:")
newlist = mylist.split()

for i in range(len(newlist)-2):
    print (i)
    temp = newlist[i]
    
    if type(temp) == str:
        newlist.pop(i)
        
print (newlist)

"""
for i in range(len(mylist)):
    if mylist[i] == int(mylist[i]):
        newlist.append(mylist[i])
    else:
        continue

print (len(newlist))
print (newlist)

"""