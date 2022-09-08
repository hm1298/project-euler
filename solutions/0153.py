#hm1289, solution from 2022
import time
import math
from itertools import permutations

def solve(n):
    """
    Provides the answer.
    """
    #quick pseudocode
    #find all primes
    #find all sums of squares
    #iterate over all numbers and fill in sums based on divisors
    prms_bool = sieve(n + 1)
    primes = [p for i in range(n + 1) if prms_bool[i]]
    sum_divisors = {p: 0 for p in primes}

    max_square = math.floor(math.sqrt(n - 1) + 2)
    for i in range(1, max_square):
        for j in range(i + 1, max_square):
            sum_squares = i * i + j * j
            if sum_squares in primes:
                #meh i need to fix this

def subset(n):
    for i in range(2 ** n):
        s = "{0:b}".format(i)
        yield ("0" * (n - len(s))) + s

def sieve(n):
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False
    prms = []
    for i in range(2, n):
        if is_prime[i]:
            prms.append(i)
            for j in range(i*i, n, i):
                is_prime[j] = False
    return prms

def is_prime(n, prms):
    if n == 1:
        return False
    for p in prms:
        if n % p == 0:
            if n == p:
                return True
            return False
    return True

def find_primes(n):
    prms = sieve(math.ceil(math.sqrt(n)) + 1)
    if prms[-1] > n:
        prms = prms[:-1]
    return prms

start = time.time()
N = 5
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))