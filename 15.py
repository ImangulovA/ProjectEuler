# How many such routes are there through a NxM grid? As number of ways can be very large, print it modulo.
import math

q = int(input())
for i in range(q):
    n,k = input().strip().split(' ')
    n,k = int(n),int(k)
    answer = math.factorial(n+k) // (math.factorial(n) * math.factorial(k))
    answer = (answer % (10**9 + 7))
    print(answer)
