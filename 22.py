#You are given around five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
#For example, when the list in sample is sorted into alphabetical order, PAMELA, which is worth 48, is the 5 name in the list. So, PAMELA would obtain a score of 240.

def numstr(string):
    return sum([ord(c)-64 for c in string])

N = int(input())
names = []
for i in range(N):
    names.append(input())
names = sorted(names)
Q = int(input())
for i in range(Q):
    name = input()
    name = (names.index(name)+1)*numstr(name)
    print(name)
