# First line contains N, next N lines contain a 50 digit number each.
# Work out the first ten digits of the sum of N 50-digit numbers.



import sys

t = int(input().strip())
sum = 0
for a0 in range(t):
    n = int(input().strip())
    sum += n
sum_string = str(sum)
print(sum_string[:10])
