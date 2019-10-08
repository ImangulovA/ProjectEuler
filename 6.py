# Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.


import sys

def sum_k_n(k,n):
    return ((n+k)*(n+1-k))//2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pyr_sum = (n*(n+1)*(2*n+1)) // 6
    sq_sum = ( (n*(n+1))/2 ) ** 2
    print(int(sq_sum-pyr_sum))

