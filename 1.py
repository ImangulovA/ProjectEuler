#!/bin/python3

import sys

def sum_till_n(n): 
    return (n*(n+1))//2

def multiple_sum(n):
    thirds = (n-1)//3
    thirds = sum_till_n(thirds)

    fifs = (n-1)//5
    fifs = sum_till_n(fifs)

    fith = (n-1)//15
    fith = sum_till_n(fith)

    return int(thirds*3 + fifs*5 - fith*15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(multiple_sum(n))
