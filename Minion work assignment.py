# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:38:35 2022

@author: Avinash Kumar

Description - Minion work assignment
"""
def solution(data, n): 
    if n == 0 or len(data) >= 100 or len(data) < 1:
        return []
    record = []
    res = []
    for i in data:
        if i in record:
            continue
        if i in res:
            res.append(i)
        elif data.count(i) > n:
            record.append(i)
        else:
            res.append(i)
    return res

data = [1,4,10,10,10,3,3,3,3,3,2,1,5,7,4]
n = 3
print(solution(data, n))