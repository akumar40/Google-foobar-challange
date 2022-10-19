# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 01:00:48 2022

@author: Avinash Kumar
"""

def solution(l):
    if len(l) < 3 or len(l) > 2000:
        return 0
    
    map = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                map[i] += 1
                count += map[j]
    
    return count

l = [1, 1, 1]
print(solution(l))