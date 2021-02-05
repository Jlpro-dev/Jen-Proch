# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:20:20 2020

@author: jenpr
"""

#even number function
#practice writing functions

def even_numbers(number = 2):
    n = int(input("Please pick a number.")) #pulls input for "n" number
    for i in range(1, n):
        if(i%2==0) and i!=0:
            print(i)

        
even_numbers()

def evens(number = 2):
    list = []
    for i in range(number +1):
        if not i%2 and i=0:
            

