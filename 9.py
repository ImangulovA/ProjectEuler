#!/bin/python3

import sys

def lint(n):
    if type(n) == int:
        return n
    else:
        return int(n)+1

def isPythagor(n):
    answer = -1
    for a in range(1,lint(n/3)):
        b = (n*n - 2*n*a)/(2*n - 2*a)
        c = n - a - b
        if b.is_integer():
            if b > 0:
                if c > 0:
                    if(c**2 == a**2 + b**2):
                        answer = int(a*b*c)
    return answer

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(isPythagor(n))
