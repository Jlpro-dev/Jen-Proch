# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:22:42 2020

@author: jenpr
"""

for i in range(1,101):
    if i%3 ==0 and i%5==0:
        print ("FizzBuzz")
    elif i%3 ==0: 
        print ("Fizz")
    elif i%5 ==0:
        print ("Buzz")
    else:
        print (i)