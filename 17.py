# Given a number, you have to write it in words.

unit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
ten = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

unit = [unit[0]] + [i[0].upper() + i[1:] for i in unit[1:]]

teen = [i[0].upper() + i[1:] for i in teen]

ten = ten[:2] + [i[0].upper() + i[1:] for i in ten[2:]]

def thou_to_word(n):
    thou_word = []
    if n//100 > 0:
        thou_word.append(unit[n//100]+' Hundred')
    n = n%100
    if 10 <= n < 20:
        thou_word.append(teen[n%10])
    else:
        if n // 10 > 0:
            thou_word.append(ten[n//10])
        if n % 10 > 0:
            thou_word.append(unit[n%10])
    return thou_word

def hard_word(n):
    whole_word = []
    if n // (10**12):
        whole_word = whole_word + thou_to_word(n // (10**12))
        whole_word.append('Trillion')
    n = n % (10**12)

    if n // (10**9):
        whole_word = whole_word + thou_to_word(n // (10**9))
        whole_word.append('Billion')
    n = n % (10**9)

    if n // (10**6):
        whole_word = whole_word + thou_to_word(n // (10**6))
        whole_word.append('Million')
    n = n % (10**6)

    if n // (10**3):
        whole_word = whole_word + thou_to_word(n // (10**3))
        whole_word.append('Thousand')

    n = n % (10**3)
    whole_word = whole_word + thou_to_word(n)
    return ' '.join(whole_word)

q = int(input())
for i in range(q):
    n = int(input())
    print(hard_word(n))
