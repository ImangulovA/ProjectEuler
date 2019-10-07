# Enter your code here. Read input from STDIN. Print output to STDOUT
def fiboword(a,b,n):
    lena = len(a)
    lenb = len(b)
    digits = [lena, lenb]
    digit_range = True
    while digit_range:
        digits.append(digits[-1] + digits[-2])
        if digits[-1] >= n:
            digit_range = False

    while len(digits) > 3:
        if n <= digits[-3]:
            digits.pop()
            digits.pop()
        else:
            n = n-digits[-3]
            digits.pop()   

    if len(digits) == 3:
        if n <= digits[-3]:
            return(a[n-1])
        else:
            n = n-digits[-3]
            return(b[n-1])
    else:
        return(b[n-1])

iters = int(input())

for iterate in range(iters):
    a,b,n = input().strip().split(' ')
    n = int(n)
    answer = fiboword(a,b,n)
    print(answer)
