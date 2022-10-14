# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 00:08:48 2022

@author: Avinash Kumar
"""
def solution(n):
    n = int(n)
    if n <= 1 :
        return 0
    count = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        count += 1
    return count
    
    
    
n = 15
print(solution(n))