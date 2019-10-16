 #Find the coefficients, a and b , for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
 
 from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def find_primest(a,b):
    n = 0
    while isPrime(n*(n+a) + b):
        n+=1
    return (n+1)

def keywithmaxval(d):
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

NUMB = int(input())

primes = [1,2]
for i in range(3,NUMB+1,2):
    if isPrime(i):
        primes.append(i)

primerow_dict = {}
longest_prime = 1
for i in range(1,NUMB+1,2):
    for k in primes:
        prnum = find_primest(i,k)
        if prnum > longest_prime:
            primerow_dict[i,k] = prnum
            longest_prime = prnum
        prnum = find_primest(-i,k)
        if prnum > longest_prime:
            primerow_dict[-i,k] = prnum
            longest_prime = prnum 

a = (keywithmaxval(primerow_dict))
print(f'{a[0]} {a[1]}')
