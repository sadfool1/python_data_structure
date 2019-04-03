#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:37:45 2017

@author: jameselijah
"""
import time
start_time = time.clock()
def r_fibonacci(n):
    if n < 2 : #BASE EQN
        return n
    else:
        return (r_fibonacci(n-1)) + (r_fibonacci(n-2)) #GENERAL EQN
print ("r_fibonacci is: ", r_fibonacci(10), end='')
print (" with a runtime of:" + str(time.clock() - start_time))
print ('')
print ('')

def i_fibonacci(n):
    if n == 0: #BASE
        return 0
    elif n ==1:
        return 1 #BASE
    result = 0
    for i in range(0,n): #GENERAL EQN
        result = i_fibonacci(n-1) + i_fibonacci(n-2)
    return (result)
print ("i_fibonacci is: ", i_fibonacci(10), end='')
print (" with a runtime of :" +str(time.clock() - start_time))

### FROM THE RESULTS ABOVE shows that the recursive function is 
### faster than the iterator by a huge factor #######

#FIBONACCI TREE FOR r_fibonacci
#                                                         r_fibonacci(5)
#                                          r_fibonacci(4)     +       r_fibonacci(3)
#                         r_fibonacci(3)  +     r_fibonacci(2)                     r_fibonacci(2) +  r_fibonacci(1)
#          r_fibonacci(2)+ r_fibonacci(1)          r_fibonacci(1) +  r_fibonacci(0)        r_fibonacci(1) +  r_fibonacci(0)
# r_fibonacci(1) +  r_fibonacci(0)
# 
''' TEST BOTH TO SEE WHICH IS FASTER '''
