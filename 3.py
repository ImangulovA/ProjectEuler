# What is the largest prime factor of a given number ?


import sys

def check_if_prime(n):
    for i in range(3,int(n**0.5+1)+1,2):
        if n%i == 0:
            return False
    return True

def largest_prime(n):
    the_largest = 1
    if n%2 == 0:
        the_largest = 2
        while n%2 == 0:
            n = int(n/2)
    factors = []
    for i in range (3,int(n**0.5+1)+1,2):
        if (n%i == 0):
            factors.append(i)
            factors.append(int(n//i))
    if len(factors) == 0:
        if n > the_largest:
            the_largest = n
    else:
        factors = list(set(factors))
        for factor in factors:
            if check_if_prime(factor):
                if factor > the_largest:
                    the_largest = factor
    
    return the_largest


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime(n))

