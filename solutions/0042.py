#hm1289, solution from 2017

def alpha_value(word):
    ans = 0
    for c in word:
        ans += ord(c) - 64
    return ans

def coded_triangle_numbers(words):
    tris = set([i * (i + 1) / 2 for i in range(1, 20)])
    total = 0
    for word in words:
        if alpha_value(word) in tris:
            total += 1
    return total

f = open('0042_words.txt')
print(coded_triangle_numbers([w.strip('"') for w in f.read().split(',')]))