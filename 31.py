#How many different ways can N p be made using any number of coins? As the result can be large print answer mod

k = int(input())
ways = [0]*100001
ways[0] = 1
for x in [1,2,5,10,20,50,100,200]:
    for i in range(x, 100001):
        ways[i] += ways[i-x]
for i in range (k):
    l = int(input())
    print (ways[l]%(10**9+7))
