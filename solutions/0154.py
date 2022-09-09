#hm1289, solution from 2022
import time

def solve(n, arr):
    """
    Needs some major efficiency improvements. Just brute forces through
    everything; best bet at improving time is throwing out cases in the
    for loop for NT reasons. We already exploit symmetry but that's a
    reduction by a factor of 6, and we need a further ~20 or better.
    """
    x = len(arr)
    fact_divs = [[0] * x]
    for i in range(1, n + 1):
        fact_divs.append([fact_divs[i - 1][j] + num_divs(i, arr[j][0]) for j in \
            range(x)])

    ans = 0
    max_a = (n + 3 - (n % 3)) // 3
    for a in range(0, max_a):
        max_b = (n - a + 2 - ((n - a) % 2)) // 2
        for b in range(a, max_b):
            c = n - a - b
            for k in range(x):
                if fact_divs[n][k] - fact_divs[a][k] - fact_divs[b][k] - \
                fact_divs[c][k] < arr[k][1]:
                    break
            else:
                if a == b and a == c:
                    ans += 1
                elif a == b or a == c or b == c:
                    ans += 3
                else:
                    ans += 6

    return ans

def num_divs(n, p):
    """
    Returns the exponent of p in the prime factorization of n.
    """
    ans = 0
    while n % p == 0:
        n /= p
        ans += 1
    return ans

start = time.time()
N, prime_factorization = 200000, [[2, 12], [5, 12]]
print(solve(N, prime_factorization))
print("Elapsed time: {:0.4f}".format(time.time() - start))