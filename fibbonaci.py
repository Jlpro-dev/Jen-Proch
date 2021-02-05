# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:35:32 2020

@author: jenpr
"""

def fibbonaci(n):
    if n==1:
        return n
    else:
        return n-2 + fibbonaci(n-1)
    
num = int(input("Pick a positive number."))
if num > 0:
    print("The", num, "th Fibbonaci number is", fibbonaci(num))    