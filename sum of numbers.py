# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:33:02 2020

@author: jenpr
"""
#sum of numbers

number = int(input("Enter any number : "))

if number < 0:
    print("ERROR")

number_sum = 0
for i in range(1, number + 1):
    number_sum += i
if number >=0:
    print("\nSum of numbers between 1 and", number, "is: ", number_sum)
    
