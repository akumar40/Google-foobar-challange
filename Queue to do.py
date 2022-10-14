# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:28:01 2022

@author: Avinash Kumar
"""

def XOR(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def solution(start, length):
    if start < 0 or length < 0:
        return 0
    if start + (length * length) - 1 > 2000000000:
        return 0
    if length == 1:
        return start
    val = XOR(start + 2*(length-1))
    if start > 1:
        val = val ^ XOR(start - 1)
    for i in range(length-2):
        elems = length - 2 - i
        init = start + length*(2 + i) - 1
        val = val ^ XOR(init + elems) ^ XOR(init)
    return val

start, length = 17, 4
print(solution(start, length))