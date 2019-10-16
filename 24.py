# What is the N lexicographic permutation of the word abcdefghijklm?

import math

def permut_num(number_of_perms):
    number_of_perms -= 1 
    
    permut = ''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    
    for i in range(12,0,-1):
        permut = permut + letters.pop((number_of_perms // math.factorial(i)))
        number_of_perms = number_of_perms % math.factorial(i)
    permut += letters.pop()

    return permut

for _ in range(int(input())):
    print(permut_num(int(input())))

