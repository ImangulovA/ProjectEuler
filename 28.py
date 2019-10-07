# TASK AT https://www.hackerrank.com/contests/projecteuler/challenges/euler028/problem

for _ in range(int(input())):
    N = int(input())
    # sums of all 4n^2 - 6n + 6 at all 
    n = (N+1)//2
    sums = (4*n*(2*n+1)*(2*n-1))//3
    sums -= 6*n*n
    sums += 6*n
    ## workaround for 1st square = 1
    sums -= 3
    print(sums%(10**9 + 7))