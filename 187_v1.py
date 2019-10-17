def howmanyfactors(n):
    factors = 0
    for i in range(2,3):
        while n%i==0:
            factors+=1
            if factors>2:
                return factors
            n = n//i
            #print(i)
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            factors+=1
            if factors>2:
                return factors
            n = n//i
            #print(i)
    if n>1:
        factors+=1
    return factors

def howmanysemiprimes(R):
    answ = 1
    for i in range(5,R):
        if howmanyfactors(i)==2:
            answ+=1
            #print(i)
    return answ

def semiprimes(R):
    answ = [4]
    for i in range(5,R):
        if howmanyfactors(i)==2:
            answ.append(i)
            #print(i)
    return answ
        
Rs = []
for _ in range(int(input())):
    Rs.append(int(input()))

answ = semiprimes(max(Rs))
for R in Rs:
    print(len([i for i in answ if i < R]) )
