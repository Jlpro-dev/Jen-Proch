# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:52:10 2020

@author: jenpr
"""

population_ages = [81, 100, 1, 9, 49, 64, 4, 9, 16, 25, 36]
#mean
n= len(population_ages)
mysum = sum(population_ages)
mean = mysum/n
print("The mean is", mean)
#median
population_ages.sort()

if n%2 ==0:
    median1 = population_ages[n//2]
    median2 = population_ages[n//2 -1]
    median = (median1+median2)/2
    
else:
    median = population_ages[n//2]
print ("The median is", median)

#mode
mode_counter = 0
for i in population_ages:
    if population_ages.count(i)>mode_counter:
        mode_counter = population_ages.count(i)
        mode=i
for i in population_ages:
    if population_ages.count(i) == mode_counter and i not in mode:
        mode.append(i)
print("The mode is", mode)