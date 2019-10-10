import math

u0,b=input().strip().split(' ')
# L, R = int(L), int(R)
u0,b=float(u0),float(b)
u1 = math.floor(2**(b-u0**2))*10**(-9)
us = [u0, u1]
for i in range(10**3):
    u0 = u1
    u1 = math.floor(2**(b-u0**2))*10**(-9)
    us.append(u1)
print('{:.9f}'.format(us[-1]+us[-2]))
