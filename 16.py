# What is the sum of the digits of the number 2^N?
q = int(input())
for i in range(q):
    poww = int(input())
    poww = 2**poww
    result = 0
    while poww:
        result += poww%10
        poww //= 10
    print(result)
