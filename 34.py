# Find the sum of all numbers below N which divide the sum of the factorial of their digits.


import math
facdict = {}
for i in range(10):
    facdict[i] = math.factorial(i)
def factosumeq(n):
    fasum = 0
    k = n
    while n:
        fasum+=facdict[n%10]
        n = n//10
    return fasum%k == 0
    
N = int(input())
our_nums = 0
for i in range(10,N):
    if factosumeq(i):
        our_nums+=i
print(our_nums)