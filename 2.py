# By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.

import sys
def even_fibo_sum(n):
    #fibon = [1,2]
    if n<2:
        return 0
    fibo1 = 1
    fibo2 = 2
    summa = 2

    while (2*fibo1+3*fibo2) < n:
        fibo1,fibo2 = 2*fibo2+fibo1,3*fibo2 + 2*fibo1
        summa+=fibo2

    return summa

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(even_fibo_sum(n))

