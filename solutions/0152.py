#hm1289, solution from 2022
import time
from itertools import chain, combinations

def solve(n, frac):
    """
    .
    """
    ans, options, stack = 0, [], [(2)]

    dct = {n: n ** -2 }
    for k in range(n - 1, 1, -1):
        dct[k] = dct[k + 1] + k ** -2

    error_bound = 10 ** -6

    not_options = set()

    for p in primes_less_than(n + 1):
        k, x = 1, p
        while x <= n:
            k, x = k + 1, p * x
            to_test = [i * x for i in range(1, (n + p - (n % p)) // p) \
            if i % p != 0]
            sieve(to_test, frac, p, k)


    while stack:
        attempt = stack.pop()

class Fraction():
    def __init__(self, numer, denom):
        k = self.gcd(numer, denom)
        self.numerator = numer / k
        self.denominator = denom / k

    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        while b != 0:
            a, b = b, a % b
        return a

def primes_less_than(n):
    """
    Returns a list of primes less than n.
    """

def sieve(arr, frac, p, k):
    """
    Returns a list that is a sublist of the input, containing all entries
    that are not ruled out.
    """
    sieved_entries = set()
    i, n = 1, len(arr)
    while i < 2**n:
        j, subset = i, []
        for k in range(n):
            j, r = divmod(j, 2)
            if r == 1:
                subset.append(arr[k])
        

start = time.time()
N = 80
print(solve(N))
print("Elapsed time: {:0.4f}".format(time.time() - start))