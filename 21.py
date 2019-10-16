#Evaluate the sum of all the amicable numbers under N.
#https://www.hackerrank.com/contests/projecteuler/challenges/euler021/problem


def factors_of_num(n):
    sum_of_factors=1
    for i in range(2,int(n**0.5+2)):
        if n%i == 0:
            sum_of_factors+=i
            sum_of_factors+=(n//i)
    return sum_of_factors

q = int(input())
amicable_numbers = []
ns = []
for _ in range(q):
    ns.append(int(input()))
maxns = max(ns)
skips = []
for i in range(maxns):
    if i in skips:
        continue
    k = factors_of_num(i)
    if i == factors_of_num(k):
        if i!=k:
            amicable_numbers.append(i)
            amicable_numbers.append(k)
            skips.append(k)
for n in ns:
    print(sum([an for an in amicable_numbers if an<n]))
