What is the Nth prime number?


import sys
from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prime_append(n,primes):
    n -= len(primes)
    i = primes[-1]
    while n > 0:
        i += 2
        if isPrime(i):
            n -= 1
            primes.append(i)
    return primes
    

t = int(input().strip())
primes = [2,3]
for a0 in range(t):
    n = int(input().strip())
    if (len(primes) < n):
        primes = prime_append(n, primes)
    print(primes[n-1])

