# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:27:30 2020

@author: jenpr
"""

#palindrome
#practice writing functions
#gather string input
print("Palindrome checker:")
def palindrome():
    astring = input("Please write a word or phrase:")
    print(astring)
#make all lowercase
    lowerstring = astring.lower()
#remove white spaces from phrase and check
    spaceless = lowerstring.replace(" ","")
#set to reverse
    reverse = "".join(reversed(spaceless))

#check if reverse = original
    if (spaceless == reverse):
        return True
    return False

print(palindrome())