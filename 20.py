# Find the sum of the digits in the number N
import math

for _ in range(int(input())):
    n = int(input())
    digisum = 0
    n = math.factorial(n)
    while n:
        digisum += n%10
        n = n//10
    print(digisum)
