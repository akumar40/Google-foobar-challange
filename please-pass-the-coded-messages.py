# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:00:54 2022

@author: Avinash Kumar
"""

from itertools import combinations

def solution(l):
    if any(i > 9 for i in l):
        return 0
    l.sort(reverse=True)
    for i in reversed(range(1, len(l) + 1)):
        nums = list(combinations(l, i))
        for num in nums:
            temp = int(''.join(map(str, num)))
            if temp % 3 == 0:
                return temp
    return 0
        
l = [3, 1, 4, 1]
print(solution(l))